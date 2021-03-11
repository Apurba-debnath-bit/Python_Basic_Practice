#--------Creating sets----------------------
#-----Note: sets are unordered collection of objects----
#There are two ways to create set or define set in python:
#using set() as constructor
#using second brackets:{}
a = set(["a","b","c", 23.4, False, 34])
#but the set constructor takes any iterable objects like set, tuple, list, dictionary etc.
print("all element of set a: ",a,"\n")
#another way to creating set:
fruits = {"orange", "mango", "apple", "banana"}
#set is changeable or mutable:
w = set({"love", "is", "blind"})
print("adding 2 set: or updating one set by adding new set to it:")
fruits.update(w)
print("The result is: ",fruits )
print("\n\n\n")
name_age = ["apu",23, "shuvra", 45, "ap",34]#update method can takes list
name = ("apu", "apu", 23, 24, 45.7, 45.7)
fruits.update(name_age)

print("after update fruits as list: ",fruits,"\n")
fruits.update(name)
print("after update fruits as tuple: ",fruits,"\n")

print("now friuts is: ", fruits)
#--------------------Remove------------------------
#To remove an item from set:
# use discard or remove method
#using remove method:
#note: if the item doesn't exist remove method will raise an error:

fruits.remove("orange")

print("after remove",fruits )
#note: if the item doesn't exist discard() method will not raise an error:
fruits.discard("kaka")
print("discard method: ",fruits)

#pop() method:
#when use pop method it removes the last item from the set:
#but, as sets are unordered, we don't know which items gets remove:
print(a)
a.pop()
print("after pop", a)
#clear() method to empty the set
a.clear()
print(a, "\n")
#The del keyword will delete the set completely:
del a
#print(a)now a isn't define

#----------Loop set---------
print("Loop through the set items: ")
for x in fruits:
    print(x)

#--------------Join sets---------------
print("\n\n Join sets: ")
#union methods
#The union() method returns a new set with all items from both sets:
a = {"shuvra","shuvra","shuvra","shuvra", "apurba", "puja", "rothosri","pallbai", 12.3, 34.5}
b = {12, 13, False,False,False, 56.8,789.0}
c = a.union(b)
print(c)
#union works similiar as update method:
#The update() method inserts the items of set2 into set1:

set1 = {"apu","ram","puja"}
set2 = {12.3, 23, 34}
set1.update(set2)
a.update(b)
print("after updating a: ",a)
print("\nusing upadte method", set1)

#Note: Both union and update method exclude any duplicate items:

#Another methods:
print(" another methdos: \n")
#intersection_update():
#intersection_update(): only keep the common items from sets insts
x = {"apple", "bananna", "cherry"}
y = {"Microsoft", "Google", "Amazon", "apple"}
#it doesn't return any new set it just only keep common the values from multiple sets:

#intersection_update method change the existing value of x:
x.intersection_update(y)
print("intersection_update() method change the existing value of x:")
print("from intersection_update method",x)


#_____________intersection() METHOD____________:

#intersection() method returns a new set , which only contains the items those are present in both sets.
#intersection() method returns only the common values:

j = x.intersection(y)#will return a new set.
print("from intersection method",j,"\n\n")
#-----adding value to y-------
y.add("bananna")
y.add("cherry")

print("Now the value of y is:---- ",y)
print("now x is: --", x)#for intersection_update method x value has changed.
#-------adding a new set to x-------
s = {"bananna", "cherry", "Rahim"}
x.update(s)
print("After updating x set with set s: --->",x )
k = y.intersection(x)#will return a new set.
print("From intersection method :  --k is",k)
#intersection method will return a new set with the common values from all sets.

#another update method:------------------
#----------symmetric_difference_update()-----------
#----it keeps only uncommon values from multiple sets:-----
#---------symmetric_difference()----------------
#----it returns only uncommon values as a new set (from multiple sets):-----

#-------------symmetric_difference_update()--------
print("----------symmetric_difference_update---------: ")
x.symmetric_difference_update(y)
print("only uncommon values kept in x (from 2 sets x and y) :-------->",x)

#-------------symmetric_difference()--------
print("-----symmetric_difference()------------")
print("now x is: ", x)
print("now y is: ", y)
print("It will return a new set with all uncommon values from 2 sets: ")
c = x.symmetric_difference(y)#it will return none
print("Using symmetric_difference() : the uncommon values are: ==> ", c)
#-----------------printing length of a set ----------------
print("printing length of a set")
print("The length",len(c))
#----------To copy an existing set---------------
print("To copy an existing set using copy method: ")
car = {"volvo", "Toyota", "Itali"}
x = car.copy()
print("after copy ",x)
#-----------------To comparing sets -------------------------->>>>>
#----------difference() Method----------
"""
this method only returns a new set with (all the different/uncommon  values comparing other set)
"""
car2 = {"rahim_car", "Karim_car", "jasim_car", "Borna_car","apur_car"}
car3 = {"rahim_car", "Karim_car", "jasim_car"}

car4 = car2.difference(car3)
print("After getting new set with uncommon values: ", car4)

##----------difference_update() Method----------
"""
this method will only keep all the different/uncommon  values comparing other set)
"""
car2.difference_update(car3)
print("After update the only difference values: comparing with other set ",car2)
#--------Comparison of two sets as their element---------->
#--------------------issubset()---------
#----------another method: issuperset()---------
#it returns a boolen value: False or True
print("\n\n")
print("Comparison of two sets as their element-\n")
print("it returns a boolen value: False or True: ----->")
v = {4, 5, 6}
#v set is a subset of b set bcz, all element of v set are present in b set
b = {5,7, 8, 0, 4, 6}
subset = v.issubset(b)
superset = b.issuperset(v)
not_super = v.issuperset(b)
dis_joint = v.isdisjoint(b)#v er modhe b er kono item ache kina?
# na thakle True r thakle False
#set.issubset(set)
print("All elements are present: as subset considering ",subset)
print("All elements are present: as superset considering ",superset)
print("Not super: ", not_super)
print("after used isdisjoint method: ", dis_joint)

#----------To copy an existing set---------------

#----------All methods of set in python----------
"""
    Characteristic of python set:------------>>>
    1. sets are unordered, unindexed, unchangeable, not allowed duplicates values
    2. Set items can be of any data type.
    3. sets are defined as objects with the data type 'set':
    4.It is also possible to use the set() constructor to make a set.
    --Measuring the Length of a set --------
    len()-> it measures the total items of a set.
    
    ---To add items to set------
    add -> add one new item to a set
    update-> to update a existing set with any iterable object(list, tuple, dict)
    union-> to join two set
     ---To remove items to set------
    del -> delete a existing set completely
    remove-> to remove an existing item from a set
    discard-> to remove an existing or non-existing item ,
    but will not arise error
    clear-> it removes all elements from a set
    #and kept it as a blank set
    pop-> it just only remove the last value of a set, 
    but set is an unordered collection of objects, 
    so we can not find out which item will delete.
    
    ---To kept common items to set------
    intersection-> it will return a new set with all common values from 2 sets
    intersection_update-> it will just update and kept the all common values from 2 sets.
    #it change the previous value of a set and kept new common values to it.
    
    ---To kept uncommon items to set------
    symmetric_difference_update()->it  will kept only uncommon values from both sets
    symmetric_difference()-> it will return a new set with all uncommon values from both sets.
    
    --To copy an existing set----
    copy()-> to copy an existing set
    
    ----Comparision of two set as their elements:--------
    issubset()-> it returns either True or false , 
    if all items of one set present in other set than True either returns False
    
    issuperset()-> it returns either True or false , 
    if all items of one set present in other set than True either returns False
    
    isdisjoint()->it returns either True or false ,
    Returns True, if no item is present in another set
    Returns False, if one or more item is present in other set
    
    
"""
#print(car2)