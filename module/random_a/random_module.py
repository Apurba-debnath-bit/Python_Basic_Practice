import random
#---------Generating floating point number-------------
# Random number generate at given range ( floating point ) number---------#
# @floating point number--------
value = random.random()#value start from 0 to 1 as floating point number.
value2 = random.uniform(0,1)#it will return a float number between 0 and 1  
range_a = random.uniform(1,23)##it will return a float number between 0 and 1 

# print("value2 : ", value2)
# print("range is: ", range_a)
# print(list_item, " Hi! ")
# print(value, "--a number from 0 to 1")

#------For any iterable object---------
gretings = ["Apu", "Apurba", "partho", "Asikur", "Asirman"]

#for a list
list_item = random.choices(gretings)#it will return a item from a list of items or from any  iterable
#for a string: 
gh = "Apurba"
ty = random.choices(gh)
#for loop iteration from 0 to 10
# for i in range(10):
#     print(, " hi! ")

# for a tuple:


#----------Random number generator for integer-----------------
value3 = random.randint(2,33)
print("random integer: ", value3)

#using for loop iteration:
for u in range(10):
    print("float -> 0 to 1: ",random.random())
print()
for i in range(10):
    print(random.randint(0,100))
print()
for y in range(10):
    print(random.choices(gretings))
print()
for t in gretings:
    print("last-try: ",random.choices(t))
print()

color = ["Red", "Dark", "purpule", "Green"]
print(random.choices(color, weights=[18,18,18,2], k = 13))

#list of range
deck = list(range(1, 53))
print(deck)
print("Suffeling a list: ")
random.shuffle(deck)
print(deck)
hand = random.sample(deck, k = 5)
print("five sample from a random list: ", hand)


