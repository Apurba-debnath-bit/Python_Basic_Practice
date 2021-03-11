#Python List are used to store multiple items in a single variable:
#We can define List in two ways :
#1. Using curly brackets and using list constructor :
#{} and list()

#python list is ordered, changeable, indexable,
#Python list allows duplicates values:
#Example of python list:

mylist = ["Apple", "Banana", "Orange"]
print("Mylist is: ",mylist)
mylist2 = list(["Apple","Banana","Banana", "Pineapple"])
print("mylist2 is: ", mylist2)
for x in mylist2:
    print(x)

#List and Tuple allows duplicate values:
#set and dictionary doesn't allow duplicate values:

#To determine how many items a list has, use the len() function:
print(len(mylist2))
#List items can be of any data type:
name_age= ["apu", 23, "apurba", 23.45, False, True,{"a","b","c","d"},("sdf",123.45),[34,45,56,67]]
print(name_age)
#name_age : list conatins string, boolean, integer, set, tuple data type.

st = ["apu","mango","tiger"]
bo = [True, False, True,False]
inti = [12, 23, 45]
fl = [34.9, 45.6, 67.7 , 67.8]
set1 = [{"2","a","b"},{"ka","kha"},{"d","f",23.4}]
tuple1 = [(1,2,3),(56,56,78),(45,56)]
print(set1)
print(tuple1)
#From Python's perspective, lists are defined as objects with the data type 'list':
print(type(set1))
print("---------------complete------------------")
#--------------Access List Items-----------
print("\n")
print("Access List items: ")

list1 = ["apple","banana","chery"]
print("Index position: 1 -> ",list1[1],"Index position: 0 -> ",list1[0],"Index position: 2 -> ",list1[2])
#if we provide exceed index, than python interpreter will arise error: index out of range
#--------print(list1[5])-----#exceed index
#we can also use negative index to access a list
#negative index means start from the end:
#-1 refer to last items and -2 refer to 2nd last item:
print("using negative index",list1[-1])
print("using negative index",list1[-2])
if "apple" in list1:
    print("yes! you are true")
#---------Slicing List-----------
print()
print("<-----------------Slicing list: ------------>")

print("List is nothing but a collection: ")
list2 =["car1","car2","car3","fuck",45.6, False]
a = list2[:]#slicing return a new list
b = list2[2:]
c = list2[3:6]
d = list2[:4]
e = list2[-4:-1]
print(a)
print(b)
print(c)
print(d)
print(e)
#--------Change List Items------
#list2.insert(0,"volvo")
#list2[1]="Honda"
#list2[-1]="Rathi"
list2[0:4]=["Honda","Kawasiki","volvo2","Acer"]
print("After value changing of a list: ",list2)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[0:3]=["valo na","Kola","misty_fol"]
print(thislist)

#if we inserted more item than replace , then the remaining item will be moved to next index position:
thislist[2:3]=["Rosogolla"]
print("index 2 position change: ",thislist)
thislist[2:3]=["Rosogolla", "Chomchom"]
print("After adding more values than replacing: ", thislist)

#insert a value in a specific index position of a list:
#using insert() function
mylist3 = [45,56,78,90,"Apurba","puja","Rathasri","Pallabi"]
mylist3.insert(0,123)
print("After inserting values",mylist3)

#-------Add list item--------
#add an item to the end of the list use append() method:
mylist3.append("Sagor")
print("After append", mylist3)
mylist3.insert(3,"hulu")
print("After insert", mylist3)
#insert and append method doesn't replace :

#----------extend method()---------------
#extend method used for any iterable object.
num = [23,45,56.7,78,89]
name=["apu","puja"]
#num.extend(name)
num.append(name)
print("after extend : ",num)
print("after append: ",num)
#here, extend method just extend the items of a list from any iterable object(set,tuple,list,dict)
n = {"sara","lala","kuku",9090}
num.extend(n)
print("after add iterable: ", num)

#----------Remove List item-----------
#------In order to remove list item, there are several methods:-----
#1. remove()
#2. pop()
#3. clear()
#4.del

#----------remove()--------
#Remove method remove an specific item from the list:
k = ["omor", "masum","sara"]
k.remove("omor")
print("after remove: ",k)

#-------------pop()-----------
#by default pop() method remove the last index:
#but we can delete a specified index value with pop method:
k.pop()
print("After pop: ",k)
#pop method remove specified index:
h = ["apple","banana","orange"]
h.pop(1)
print("after pop a index: ",h)
#-------------del keyword --------------------
#del keyword also removes the specified index:
#use 3rd bracket for it:
print("before remove : ",h)
del h[0]
print("using del keyword: ", h)
#del keyword also delete the list completely:
del h
#print(h)#nameerror: name "h" is not define

#------------clear method-----------
#clear method clear all items from list and doesn't returns anything:
s = [34,56, "t","p"]
s.clear()
print(s)

#Short hand for loop in python:
#Short hand loop works for list and set collection data type.
sima = ["Rotaon","Tata","Mona","Friend"]
[print(x) for x in sima]

ty = [("a","b","c","d","e","f"), {"ty","kk"}]

[print(y) for y in ty]


#---------List comprehension------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
em = []
for x in fruits:
    if "a" in x:
        em.append(x)
print(em)
#With list comprehension you can do all that with only one line of code:
print("List comprehension: ")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [y for y in fruits if "a" in y]
print("using List comprehension: ", newlist)

#Another List comprehension example:
car_list =["volvo","tata","Toyota","Honda","popo","klkl","hundai"]
newlist2=[d for d in car_list if "o" in d ]
print("List: ->",newlist2)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]
print(newlist)
new2 = [x for x in range(10) if x < 5 ]
print(new2)

newlist = [x.upper() for x in fruits]
print(newlist)
b = [c.upper() for c in car_list]
print(b)
#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)
newlist = [x if x !='banana' else 'orange' for x in fruits]
print(newlist)

#------------sort()--------------------------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
d = ['a', 'v', 'c', 'b', 'd','e']
g = ['h', 'i', 'c', 'k', 'l','m']
d.sort(reverse=True)
g.sort()
print(d)
print(g)
#-----sort descending--------
#use attribute in sort method as perameter:
#reverse=True
dd = [23,56,67,24,45,25,26,28,1,21]
dd.sort(reverse=True)
print(dd)
#The reverse() method reverses the current sorting order of the elements.
#The reverse() method
dd.reverse()
print(dd)
#-------------Copy list --------------------
#There are two ways to copy list:
my = ["p","Q","R","S","T"]
vv = my.copy()
kk = list(my)
print("my: ",my)
print("vv: ",vv)
print("kk: ", kk)
#----------------Join List-----------------
#There are two ways to join list.----------
# 1. using concatination sign: + operator
ab =[1,2,3,45,5]
bb = ["sad","pad"]
ss = ab+bb
print(ss)
#2. Using extend() method: #extend method return none, it just update the list.
#ab.extend(bb)
#print("ab: change: ", ab)
#3. Using append()
for x in bb:
    ab.append(x)
print(ab)

#-----------------count(vlaue)---------
#Return a number of times the value 9 appears int the list:
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

#------------index()------------
#The index() method only returns the first occurrence of the value.
#What is the position of the value 32:
fruits = [4, 55, 64, 32, 16, 32]

u = fruits.index(32)
print(u)


