s1 = "APURBA"
l1 = ["eat","sleep","akas"]
#syntax: enumarate(iterable, start=0)
#enumarate object creation: 
obj1 = enumerate(s1, start=0)
obj2 = enumerate(l1, start=0)
#type checking:
print ("Return type:",type(obj1))
#enumarate object used as a--->>>> list() of tuple: 
print("enumarate object used as a--->>>> list() of tuple:----------")

print("The enumarate of obj1: ",list(obj1))
print("The enumarate of obj2: ", list(obj2))

#using for loop: enumarate object iteration 
print("Obj1 iteration using for loop:----------------- ")
for item in enumerate(s1):
    print("for loop:",item)

print()

print("Obj2 iteration using for loop:------------------ ")
for item2 in enumerate(l1):
    print(item2)

# changing index and printing separately
print("changing index and printing separately-------------")
for count, item in enumerate(l1,101):
    print("for loop: changed index: ",count, item)

print ("Return type:",type(obj1))

#source: https://www.geeksforgeeks.org/enumerate-in-python/
