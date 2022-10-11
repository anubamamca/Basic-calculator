def add(num1,num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("please select any operation:\n"
        "1.Add\n"
        "2.Subtract\n"
        "3.multiply\n"
        "4.Divide\n")
operation = int(input("Select the operation from 1 to 4:"))
num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
if operation == 1:
    print(add(num1, num2))

elif operation == 2:
    print(subtract(num1, num2))

elif operation == 3:
   print(multiply(num1, num2))

elif operation == 4:
    print(num1, "/" , num2, "=" ,divide(num1, num2))

else:
   print("invalid number,enter the operation from 1 tp 4!")





