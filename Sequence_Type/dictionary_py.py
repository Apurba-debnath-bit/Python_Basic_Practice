#In python 3.6 and earlier dictionaries are unordered:
#Dictionaries are ordered, changeable, not allowed duplicate values:

#---------Dictionary------------------------
#Dictionaries are used to store data values in key:value pairs:
#Dictionary is collection of data which is ordered, changeable and does not allow duplicate values:
#Dictionaries are written with curly brackets, and have keys and values:

#example:
thisdict = {
    "brand": "Honda",
    "model": "Xdfr",
    "year": 1998
}
print("The type is: ",type(thisdict))
print("The length: ",len(thisdict))
print("The dictionary: ",thisdict)
print(thisdict["brand"])#access values by (key name)
print(thisdict["model"])#access values by (key name)

#-------------Dictionary Items------------
#Dictionary items are ordered(upto python 3.6 version) , Changebale, not allowed duplicate values:
#Dictionary items are presented in Key:value pairs.

#note:
# As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.
#-------Changeable meaning:-------------------------
#Dictionaries are changeable, meaning that we can change,
# add or remove items after the dictionary has been created.

#------------NO Duplicate values allow in Dictionary means:-----
#meaning:
#Dictionary doesn't allow duplicate key:
#Dictionary cannot have two items with the same key:
#if we assign same key with different values than last key: value will be taken
thisdict = {
    "brand": "Honda",
    "model": "Xdfr",
    "year": 1998,
    "year": 1995,#this will taken
}
print(thisdict)

#----------------Dictionary Length--------------------
#to determine how many items a dictionary has:
#use len() function: it returns a number
length_dic = len(thisdict)
print("Length of Dictionary: ",length_dic)

#---------------Dictionary Items - Data Types-----------
#The values in dictionary items can be of any data type:
thisdict2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
    "engine": {"urt","gas","fuel"},
    "lol":("love","me")

}
print(thisdict2["lol"])
#-------------------Accessing values---------------

a ={
    "brand":"Honda",
    "model":"x-34",
    "engine":"electric",
    "color":["red","green","blue"]
    }
#There are two ways of accessing values of a dictionary:
#1.dict_name[key]
#2.dict_name.get(key)
x = a['color']
print("After accessing key: ", x)
#There is also a method called get() that will give you the same result:
#get() method also get a key:
v = a.get('brand')
print("After accessing key: ", v)
print(a["engine"])
#if we write an invalid key than we will get the key error:

#----------------Get all Keys-------------------
#------keys()------------------>return a list of all keys in a dict
list1 = a.keys()
print("all keys: ", list1)

#-------------Add a new pair to dictionary----------

car = {
    "Name": "Honda340",
    "Brand": "x-45",
    "Engine": "Auto",
    "Gear": 5,

}
#before the change:
print("Before change: ")
x = car.keys()
print("the car is: ", car)
print(x)
#Adding one (key:value) pair in dictionary:

car["color"] = ["red", "green","blue"]
car["wheel"] = [3,4]
car["aircool"]=[False,True]
print()
print("The car is: ", car)

#After change:
print("After change: ")
x = car.keys()
print(x)

#----------values()-----------------------------
#---values()-----> return a list of all values in a dictionary.
print("\n\n")
print("Printing all values: ")
list2= car.values()
print(list2,"\n\n")
count = 0
for x in car.values():
    count = count + 1
    print(f"{count}no. value: ", x)

#Add a value to dictionary:
car["year"] = 2021
print("After change : ")
count = 0
for x in car.values():
    count = count + 1
    print(f"{count}no. value: ", x)
print(car)
u = car.values()
print(u)

#replace or change the value:
car["year"]= 1991
print("\n\n")
print("change a value of dictionary: ")
print(car)
print(car["year"])
print(car.get("year"))

#-----------------items() method return each items or pair as a tuple in a list:
c = car.items()
print(c)
#items method return a list of tuples:
#each and evary tuple made of a key:value pair in a dictionary

#----------Change(Add) Dictionary item--------------
#There are two ways of changing dictionary values:
#1. accessing key with square brackets: dict_name[key] = value
#2. using update method: dict_name.update({key:value})
print("\n\n")
print("1st way: using square bracket : ")
car["Brand"] = "X-4567RR"
print(car)

print("2nd way: using update method and passing short dict on it : using")
car.update({"year":2020})
print(car)
#-------------------Delete Dictionary Item------------
#1.pop()-> pop() take a parameter of key or a specified key
#2.popitem()-> remove the last item from the dictionary
#3.clear()-> clear the dictionary
#4. del keyword dict[key]-> del keyword with a specified key
# -> delete the key:value pair or that specified item
#5. del dict(completely delete the whole dictionary)

laptop = {
    "name": "Laptop1",
    "brand": "HP",
    "Mother_board":"intel",
    "Mouse": ("red", "gr-09"),
    "R_year":2021

}
print("Removing item from a Dictionary: ")
print("Before remove: ")
print(laptop,"\n")
print("After remove: ")
laptop.pop("Mouse")
print(laptop)

#now using:
#popitem() method to delete the last item in a dictionary:
print("After using pop item: ")
laptop.popitem()
print(laptop)
#using del keyword:
#st: del dict_name[key]
#del keyword for delete a specified item:
print("Before delete: ")
print(laptop)
print("Delete Mother_board key using del keyword: ")
del laptop["Mother_board"]
print("After Delete: ", laptop)

#-----------clear() method to clear all items in a dictionary:
print("Before clear: ",laptop)
laptop.clear()
print("After clear: ", laptop)

#---------del keyword for delete the entire dictionary:
del laptop
#print(laptop)#NameError: name "laptop" isn't define

#-----------------------Copy Dictionary-------------------------
#1. using copy method-->copy()
#2. dict() constructor
#Another way to make a copy is to use the built-in function dict().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict = thisdict.copy()#coping
print("my_dict is : ",my_dict)

s = dict(thisdict)#assigning
print("s is: ",s)

#-----------------fromkeys() method --------------------in dict---
#fromkeys() method return a dictionary with specified keys and values
#syntax: dict.fromkeys(keys,values)
# here , keys are required, values are optional: by default None
print()
print("using fromkeys() method: ")
x= {"key1", "key2","key3"}
y = 0
s_dict = dict.fromkeys(x,y)
print(s_dict)

#y :
print("\n", "This is by default: ")
y = {"k1","k2","k3","k4"}
dic_56 = dict.fromkeys(y)
print(dic_56)

#So, fromkeys(keys, value)
#it returns a dictionary with specified keys and values

#-----------Loop trough dictionary-------------
for x in dic_56:
    print(x)#will print all keys from this dictionary
    print(dic_56[x])#will print all values for each key
print("values printing: \n")
for t in thisdict.keys():
    print(thisdict[t])
print("values printing: \n")
for v in thisdict.values():
    print(v)

#Both keys and values printing: using items() method
s = thisdict.items()
print(s)
print('both keys and values printing using items method: ')

for b,c in thisdict.items():
    print(b,c)
#--------------------Nested Dictionaries----------------
#A dictionary can contain dictioanry this is called nested dictionary:

family ={
    "child1":{
        "name":"Apurba",
        "age": 23
    },
    "child2":{
        "name":"Apu",
        "age": 28
    },
    "child3":{
        "name":"Sagor",
        "age": 27
    }

}

a = {
    "name": "fufa",
    "Age":  45
}
b = {
    "name": "frr",
    "Age": 67
}
c = {
    "name":"sdf",
    "Age": 67
}

family2 ={
    "a": a,
    "b": b,
    "c":c
}
print(family2)
#that means a dictionary key contains a full dictionary

# Python does not have built-in support for Arrays, but Python Lists can be used instead.