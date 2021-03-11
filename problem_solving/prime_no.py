number = int(input("Enter any positive integer number: "))
count = 0
i = 2


while i <= (number-1):
    if number % i == 0:
        count += 1
        break
    i += 1


if count == 0:
    print("Prime no")
else:
    print("Not a prime no")