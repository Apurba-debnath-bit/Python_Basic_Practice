n = int(input("Enter the ending number: "))
count = 0
i = 2
print("All prime numbers: ", end="")
while i <= n:

    j = 2
    while j <= (i-1):
        if i % j == 0:
            count = count + 1
            break
        j = j + 1
    if count == 0:
        print(i, end=" ")
    count = 0
    i = i + 1

