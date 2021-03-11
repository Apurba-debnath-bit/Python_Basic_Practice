try:
    k = int(input("Enter a number: "))
    print(k / 0)
except ZeroDivisionError as e:
    print("Hey! You cann't devide a number by zero: ",e)
except NameError as ey:
    print("The name is not defined: ",ey)
except ValueError as e:
    print("Invalid Input:  ", e )
finally:
    print("resource closed ")