print("my name is apurba", "I am 10 yrs old", 123, "love is blind", sep=" ")
print("this is : ", end=" \n hellow now i am here\n hkjjkhjj ")
print()
#Pass value as a parameter
a = "I"
b = "love"
c = "you"
print("hey", a, b, c)

#sequential formating pass value
#using formate method:
print("{0} love {1}".format(a,b))
print("{1} vemper {0}".format(b,c))
#format using a variable
print("this is {name} who is a string {name2}  ".format(name=a, name2 = b))
#passing value as tuple
print("%s love %s"%(a, c))
#passing value as dictionary:
print("%(hey)s love %(hoi)s"% {"hey":a , "hoi": b})
print("%(hello)s love %(ok)s")%{"hello":a, "ok":b}

