import requests

{
    "number": 371,
    "is_prime": False,
    "is_perfect": False,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  # sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" # gotten from the numbers API
}

number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")  # Not necessarily prime

# Check if the number is perfect
def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]  # Get divisors
    return sum(divisors) == num  # Compare sum to number

if is_perfect(number):
    print(f"{number} is a Perfect Number!")
else:
    print(f"{number} is NOT a Perfect Number.")


url = f"http://numbersapi.com/{str(number)}"  # Remove `#`
response = requests.get(url)
response.raise_for_status()  # Ensures HTTP request is successful

try:
    data = response.json()  # Try to parse JSON
except requests.exceptions.JSONDecodeError:
    data = response.text

print(data)
