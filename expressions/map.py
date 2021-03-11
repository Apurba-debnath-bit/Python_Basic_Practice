# items =[2, 4, 5, 7, 9]
# squired = []

# for x in items:
#     squired.append(x**2)

# print(squired)

items =[2, 4, 5, 7, 9]
#x er modhe sob item ekta ekta kore asbe: 
def squired(x): return x**2
#map function return a list
#map(function, sequence)
#map(aFunction, aSequence)
print("The list is: ", list(map(squired,items )))

print("lambda function printing:------------------")
l1 = [11,22,33,44,55]
print("using lambda function: ", list(map(lambda x: x**2,l1)))


