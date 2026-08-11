num1 = int(input("Enter First Number: "))
operator = input("Enter Operator: ")
num2 = int(input("Enter Second Number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    print("Invalid Operator")

print("Result:", result)