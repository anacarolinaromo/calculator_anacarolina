
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a times b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b."""
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a / b

def main():
    """Run the simple calculator."""
    print ("Simple Calculator")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")

    operation = input("Select operation (1/2/3/4): ").strip()
    while operation not in ['1', '2', '3', '4']:
        print("Invalid selection. Please choose a valid operation.")
        operation = input("Select operation (1/2/3/4): ").strip()

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if operation == '1':
        result = add(number1, number2)
    elif operation == '2':
        result = subtract(number1, number2)
    elif operation == '3':
        result = multiply(number1, number2)
    elif operation == '4':
        result = divide(number1, number2)

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()