from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Allow all origins
origins = [
    "*",
]

# CORSMiddleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)


# Define the request body model
class NumberRequest(BaseModel):
    # number: int
    number: int = Field(..., example=371)
    is_prime: bool
    is_perfect: bool
    properties: list[str]
    digit_sum: int
    fun_fact: str


def is_prime(n: int) -> bool:
    """Check if a number is prime."""        
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def get_number_properties(n: int):
    """Determine properties of the number."""
    properties = []
    if n % 2 == 1:
        properties.append("odd")
    else:
        properties.append("even")

    if sum(int(digit) ** len(str(n)) for digit in str(n)) == n:
        properties.append("armstrong")

    return properties


def get_digit_sum(n: int) -> int:
    """Calculate the sum of digits of the number."""
    return sum(int(digit) for digit in str(n))


def get_fun_fact(n: int) -> str:
    """Fetch a fun fact about the number from Numbers API."""
    url = f"http://numbersapi.com/{n}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    return "No fun fact available."


@app.get("/")
async def index():
    """Root"""
    return {
        "message": "Welcome to the Number API! 🎉",
        "properties to check": "prime, perfect, digit_sum, amstrong, fun_fact",
        "usage": "Add a number to the URL like this: /number/256",
        "example": "http://127.0.0.1:8080/number/256"
    }


@app.get("/number/{num}", response_model=NumberRequest)
# @app.get("/number/{num}")
async def number_info(num: int):
    """API endpoint to return JSON data about a number."""
    if num < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative.")
    return {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": get_number_properties(num),
        "digit_sum": get_digit_sum(num),
        "fun_fact": get_fun_fact(num)
    }
