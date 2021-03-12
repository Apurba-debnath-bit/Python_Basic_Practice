n = int(input("Enter the number of set member: "))
p= n + 2
c = 0

def real_sub(a,b):
    print( (a + b)-1)

for y in range(1,n):
    c = c + y

real_sub(p,c)

