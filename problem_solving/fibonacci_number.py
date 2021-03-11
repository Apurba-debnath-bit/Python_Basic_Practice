first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))


for x in range(0, 100):
    fibonacci_no = first + second
    # print("First No: ", first," ", end="")
    # print("Second No: ", second," ",end="")
    # print("Fibonacci_NO: "," ",fibonacci_no)
    print(f"{first} + {second} = fibo: {fibonacci_no} "," ,", end="")
    #Now second will be first no
    #fibonacci no will be socond no.
    first = second
    second = fibonacci_no

print("End loop")




