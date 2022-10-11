#nested if#

operation = int(input("Select the operation :"))
print("Enter two numbers:")
num1 = int(input())
num2 = int(input())

if operation == 1:
    add = num1 + num2
    print(add)

elif operation == 2:
    subtract = num1 - num2
    print(subtract)

elif operation == 3:
    multiply = num1 * num2
    print(multiply)

elif operation == 4:
    divide = num1 / num2
    print(divide)

elif operation == 5:
      exit()
else:
   print("invalid operation!")
