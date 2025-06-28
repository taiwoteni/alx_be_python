def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float or str: The result of the operation, or an error message for division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'. Use 'add', 'subtract', 'multiply', or 'divide'"