import operations

if __name__ == "__main__":
    a = float(input("Enter the first operand: "))
    b = float(input("Enter the second operand: "))
    operation = input("Enter the operation (sum, subtract, multiply, divide, +, -, *, /): ").strip().lower()

    try:
        result = operations.perform_operation(a, b, operation)
        print(f"The result of {operation} between {a} and {b} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

