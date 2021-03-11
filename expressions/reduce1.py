#reduce is a function of functools module
#from functools import reduce

#functools module ka ek hissa function he reduce

#sum of all list items: using for loop: 
# print("sum of all list items: using for loop: ------")
l1 = [1, 2, 3, 4, 5, 6]# 1+2 = 3 +3 = 6 +4 =10 +5 = 15+6 =21 #------reduce works like that
num = 0
for i in l1:
    num = num + i

print(f"The sum of all list items using for:  {num}")

#same work can done with reduce function:
from functools import reduce
num = reduce(lambda a,b: a+b, l1)
print("using reduce fuction sum is: ", num)
