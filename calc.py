num1 = int(input("Enter a number 1 - "))
num2 = int(input("Enter a number 2 - "))
opr = input("Enter a opr.. ")
if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("Syntax invalid .........")