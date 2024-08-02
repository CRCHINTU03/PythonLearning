
operand = input("Enter an operand (+ , - , * , / ): ")

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))


if operand == "+":
    result = num1 + num2
    print(round(result, 3))
elif operand == "-":
    result = num1 - num2
    print(round(result, 3))
elif operand == "*":
    result = num1 * num2
    print(round(result, 3))
elif operand == "/":
    result = num1 /num2
    print(round(result, 3))
else:
    print(f"you have entered an invalid operand {operand}")

