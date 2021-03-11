#variable is case sensitive
don = 123
Don = 1234
print(don)
#Two types of variable gobal variable and local variable:

a = 6
b = 3.4
f = "hasdgk"
c = (1,2, 3, 4, 5, 6)
d = {1, 2, 3, 4, 5, 6,7}
e = [1, 2, 3, "asv", 7, 9]

#Different values to one variable:
g = 4
g = 5
print(g)#printed the last value:

#concatinating variable:
v = int(a + b)
print(v)
k = "learn something everyday"
print("love "+k)#for string concatination same type must be required.
print(a,b, f, c, d, e, sep="\n")

#multiple variables in one line but same value:
s = j = i = 345
print(j)
print(s)
print(i)
print()
#different data type in same line :

w, q, n, x, z = 123, "I am q", (3,4), {5, 65, 67}, [1, 3, 5]
print(w, q, n, x, z, sep="\n")




