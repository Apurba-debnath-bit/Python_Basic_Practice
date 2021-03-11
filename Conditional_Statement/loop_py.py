n = int(input("Enter the last number: "))

for x in range(1,n+1):
    if x == 30:
        continue
    elif x == 45:
        print(x)
        break
    print(x)