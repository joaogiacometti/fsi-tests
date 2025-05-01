from enum import Enum

class Operation(Enum):
    SUM = "sum"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    ADD_SYMBOL = "+"
    SUBTRACT_SYMBOL = "-"
    MULTIPLY_SYMBOL = "*"
    DIVIDE_SYMBOL = "/"

def perform_operation(a, b, operation):
    if operation == Operation.SUM.value or operation == Operation.ADD_SYMBOL.value:
        return sum(a, b)
    elif operation == Operation.SUBTRACT.value or operation == Operation.SUBTRACT_SYMBOL.value:
        return subtract(a, b)
    elif operation == Operation.MULTIPLY.value or operation == Operation.MULTIPLY_SYMBOL.value:
        return multiply(a, b)
    elif operation == Operation.DIVIDE.value or operation == Operation.DIVIDE_SYMBOL.value:
        return divide(a, b)
    else:
        raise ValueError(f"Invalid operation: {operation}. Please use one of {', '.join([op.value for op in Operation])}.")


def sum(a, b):
    return a + b;

def subtract(a, b):
    return a - b;

def multiply(a, b):
    return a * b;

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is undefined.")
    return a / b;