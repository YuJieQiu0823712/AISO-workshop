def calculator_tool(operation: str, a: float, b: float) -> str:
    """A calculator tool that performs basic arithmetic."""
    if operation == "add":
        return str(a + b)
    elif operation == "subtract":
        return str(a - b)
    elif operation == "multiply":
        return str(a * b)
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return str(a / b)
    elif operation == "pow":
        return str(a ** b)
    elif operation == "sqrt":
        return str(a ** 0.5)
    else:
        return "Error: Invalid operation"
