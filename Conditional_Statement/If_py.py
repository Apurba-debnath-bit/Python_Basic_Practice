a = 300
b = 20
#if a > b:#condition true:
    #print("a is bigger than b")
#print("Hi")

if a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")
elif a != b:
    print("a isn't eqaul to b")
else:
    print("a is greater than b")

#------------One line if statement-------------
c = 56
d =300
#if c > d: print("c is greater than d")#Short hand if

#short hand if else statement:
print("c is bigger ") if c > d else print("not bigger")
#elif short hand:no shorthand for it

e = 120
f = 34
j = 500

if e > f and j > f:
    print("both condition are true")
if f > e or j > f :
    print("one is true")