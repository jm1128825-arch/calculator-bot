def solve(expression):
    expression = (
        expression
        .replace("×", "*")
        .replace("÷", "/")
        .replace("%", "/100")
    )

    result = eval(expression)

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return str(result)
