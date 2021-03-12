num = int(input("Jai songkhar gunitok chan ta likhun:- "))
range_of_gunitok = int(input("koto porjonto chan ta enter korun:- "))
a = 1
#s = []
d = []
for x in range(1 ,  range_of_gunitok+1):
    a = num * x
    if a <= range_of_gunitok:
        #s = s.append(a)
        d.append(a)
        print(a, end=" ")

#print("As a list: ", s)



print() 
print("List of gunoinok: ",d)