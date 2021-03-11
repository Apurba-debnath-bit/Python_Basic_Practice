my_tupel = ("a","b","c")

#Tuple is a collection which is ordered and unchangeable
#1.Tuple is ordered
#2.Tuple is unchangeable
#3.Tuple allows duplicate values
#4.Tuple items are indexed

#-----------Create Tuple With One Item--------
#--> To create a tuple with one item you have to add a comma after one item:
#--> Otherwise, python will not recognize it as a tuple

#NOT A TUPLE:
dd = ("apple")#only str.
uu = type(dd)
print(uu)
#it treated as string

#tuple:
kk = ("apple",)#recognize as tuple
print(type(kk))

#------------len() function-------------
#len() function-> used to determine how many items a tuple has:
d =("asd",)
print(len(d))

#Tuple Items - Data Types:
#Tuple items can be of any data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (1.3, 5.3, 7.4, 9, 3, True,["j","k","m"],{"i",34,45,5,"y"})
tuple4 = (True, False, False)

print("tuple1: string:  ", tuple1)
print("tuple2: integer: ", tuple2)
print("tuple3: mix: ", tuple3)
print("tuple3: boolean: ", tuple3)

#---------making Tuple---------------
#It is also possible to use the tuple() constructor to make a tuple.
#1. Tuple constructor # note the double round-brackets
# 2. () --> using round brackets.
f = tuple(({},{1,2,3},{4,5,6},["apurba","apu",123], 45.6,6,7,"puja",False))
print("new tuple is: ",f)
print(type(f))

#---------Access Tuple------
#tuple_name[index_no]
r = f[1]
#f = f[78]#IndexError: tuple index out of range
print(r)
#print(f)#IndexError: tuple index out of range

#Negative Indexing:
#-----negative indexing means start from the end:
#negative indexing means start from the end:
h = f[-1]
print(h)

#----------Range of Indexes/Slicing------------
gh =f[:-1]
gh1 = f[:]
gh2 = f[-5:-1]
gh3 = f[3:]
print(gh)
print(gh1)
print(gh2)
print(gh3)

#----------Change Tuple-----------
#Tuples are unchangeable, meaing that you cannot change, add, or remove items once the tuple is created.
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#The del keyword can delete the tuple completely:

#--------Join Two Tuples----------
#---------multiply Tuples--------
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)*4
add1 = tuple1+tuple2
num = add1.count(3)
ind = add1.index("c")
print(add1)
print(num)
print(ind)
#two built-in methods fro tuple:
#index()--return  index number or position of a value
#count()---return the total number of specific value