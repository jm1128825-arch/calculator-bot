def solve(expression):
    expression = expression.replace("×", "*").replace("÷", "/")

    return str(eval(expression))
