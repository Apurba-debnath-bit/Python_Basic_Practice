import pdb

car1 = "Volvo"
car1_price = 450000

car2 = "Honda"
car2_price = 560000

pdb.set_trace()
while True:

    choose = int(input("Enter 1 for car1 or 2 for car2:-->  "))# enter any string value:
    print(choose)

    if choose == 1:
        print(f"{car1} is cost of {car1_price}")
        break
    elif choose == 2:
        print(f"{car2} is cost of {car2_price}")
        break
    else:
        print("You must enter 1 or 2.")
        continue
