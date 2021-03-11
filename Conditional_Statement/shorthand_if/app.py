try:
    a = int(input("Enter a 1st number: \n"))
    b = int(input("Enter a 2nd number: \n"))


# if a > b : print("A is greater then B")
# if a < b : print("A is smaller then B")

#using if else or elif statement:
    print("A is greater then B") if a > b else print("A is smaller then B")
except Exception as e:
    print("Error is: ",e)

# structure: statement if condition else satement