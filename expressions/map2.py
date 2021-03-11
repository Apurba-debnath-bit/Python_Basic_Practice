#a list of function as a sequence:
def square(x):
    return x**2
#def add(num1, num2): return num1+num2
def cube(x):
    return x**3
    
func_list = [square, cube]

for r in range(5):
    value = map(lambda x : x(r), func_list)
    print(list(value), end="")

# def square(x):
#         return (x**2)
# def cube(x):
#         return (x**3)

# funcs = [square, cube]
# for r in range(5):
#     value = map(lambda x: x(r), funcs)
#     print (list(value))