firstNumber = int(input("Enter First Number: "))
secondNumber = int(input("Enter Second Number: "))
operationType = input("Enter any operator from them > '+','-','*','/','%' : ")

if operationType == "+":
    add = firstNumber + secondNumber
    print("Addition: ",add)
elif operationType =="-":
    sub = firstNumber - secondNumber
    print("Subtraction: ", sub)
elif operationType =="*":
    mul = firstNumber * secondNumber
    print("Multiplication: ", mul)
elif operationType =="/":
    div = firstNumber / secondNumber
    print("Multiplication: ", div)
elif operationType =="%":
    mod = firstNumber % secondNumber
    print("Modulus: ", mod)
else:
    print("You haven't enter any correct operator.")
