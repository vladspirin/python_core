def arithmetic(num1, num2, operation):
    result = 0
    if operation == "+":
        result = num1 + num2
    if operation == "-":
        result = num1 - num2
    if operation == "*":
        result = num1 * num2
    if operation == "/":
        result = num1 / num2
    return result
