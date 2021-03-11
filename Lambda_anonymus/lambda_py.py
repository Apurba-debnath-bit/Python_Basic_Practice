v = lambda a: a*a
print(v(4))

c = lambda a,b: a + b
print(c(3,4))

x = lambda d,f : d**2 + f**2
print(x(5,6))

u = lambda a, b, c : a + b + c
print(u(2,3,4))

def my_func(n):
    return lambda a: a * n
my_doubler = my_func(2)
my_tripller = my_func(3)
print(my_doubler(11))
print(my_tripller(11))