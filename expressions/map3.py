#converting all data of a list to int:
a = ["3","5","65"]
#this is not possible because we are trying to convert string to int:
#error: can only concatenate str (not "int") to str
#a[2] = a[2]+1

# this for loop is wrong because: it just calling each item not index position:
# for item in a:
#     a[item] = int(a[item])

#here we can use both:
# range(3) means 3 items and 0 to upto 3, --> 0,1,2..upto 3
#here we can also use len(a)
# for i in range(3):
#     # a[0] = te jai item ta ache take int e convert kore a[0] position e rakhbe
#     #this loop will iterate untill 0-1-2
#     a[i] = int(a[i])

# print(a)

# #list item has changed to int

# a[2] = a[2]+1
# print("After updating list a: ",a)

#Same work we can do with map function also:
#map function return an object of list
#first convert it to list using list() constructor
#then get the result
#map function takes 2 arguments:
#map(func, iterable)

# obj1=map(int, a)
# a = list(obj1)
# print(a[1]+1)#you just print but not changed it yet

# a[1] =a[1]+2
# print(a)

new = [2, 3, 4, 5, 6, 7, 8, 9]
square = list(map(lambda x: x*x, new))
print(square)



