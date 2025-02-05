# Number API - Stage 1 HNG task

A FastAPI-based web service that provides information about a given number, including whether it is prime, perfect, Armstrong, and more.

## Features
- Check if a number is **prime** or **perfect**
- Determine if a number is **Armstrong** or **odd/even**
- Calculate the **sum of digits**
- Fetch a **fun fact** about the number from the Numbers API - http://numbersapi.com/#34

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sevenwings26/HNGbackendIntern_stage1_NumberAPI.git
   cd number-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Start the FastAPI server with:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8080 --reload
   ```
The API will now be accessible at `http://127.0.0.1:8080`.

## API Endpoints

### 1. Home (`/`)
**Description:** Returns a welcome message and instructions on how to use the API.

**Request:**
```bash
GET http://127.0.0.1:8080/
```

**Response:**
```json
{
    "message": "Welcome to the Number API! 🎉",
    "usage": "Add a number to the URL like this: /number/371",
    "example": "http://127.0.0.1:8080/number/371"
}
```

### 2. Number Info (`/number/{num}`)
**Description:** Returns detailed information about a given number.

**Request:**
```bash
GET http://127.0.0.1:8080/number/371
```

**Response:**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Documentation
FastAPI provides an interactive Swagger UI:
- 📌 **Swagger Docs:** [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
- 📌 **ReDoc:** [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)


## CORS Handling
This API includes CORS support to allow cross-origin requests. The `CORSMiddleware` has been configured to permit requests from specified origins, methods, and headers.

## Hiring Python Developers
Looking to hire expert Python developers? Check out [HNG Python Developers](https://hng.tech/hire/python-developers).
