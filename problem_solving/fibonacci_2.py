n = int(input("How many numbers you want: "))
first = 0
second = 1
print(f"{first} {second}",end=" ")
i = 3
while i <= n:
    fiboNO = first + second
    print(fiboNO, end=" ")
    first = second
    second = fiboNO
    i += 1





