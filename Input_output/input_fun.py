#input can be given by two ways , one mouse er help nie or touch er help nie
#keyboard er help nie.
#input-> keyboard, mouse or touch

#a = input("Enter your name: ") #input function return a string
#b = float(input("Enter your age: ")) #input function return a string
##print("you are %s and your age is %d"%(a, int(b)))
#print("name: {} \nage: {} ".format(a, int(b)))

#multiple inputs in one line:
a, b, c, d, e, f = input("Enter some number: ").split()#by default split func takes a String
print("{1}, {0}, {2}, {4}, {3}, {5}".format(a, b, c, d, e, f))


