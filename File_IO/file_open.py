print("------------------------- Read with 'r' mood: -------------------------")
#We have to create a file in same directory, before opening a file:
sd = open("sogor", "r")
#print(sd.read())
print()
#After read data for loop will not work:
#using for loop for getting all data from a file:
print("using for loop for getting all data from a file:-------------------->>>>>")

# for data in sd:
#     print(data,end="")

df = open("abcd","w")
#print(df.write("Love"))

for data1 in sd:
    df.write(data1)

print("\nEnd: ")
#Read per line from a txt file:
print("Read per line from a txt file:-----------------------")
print()

f = open("sogor", "r")
print(f)#it just only return the file object
print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline())


print("------------------------- write with 'w' mood: -------------------------")

sd2 = open("Rahim", "w")
print(sd2.write("Kaku"))
print()

print("------------------------- write with 'a' mood or append mood:-------------------------")
print("Only write is possible with append(a) mood..............")
filedir = open("fileName.txt","a")
print(filedir.write(" Asdf"))

print("-------------------------By deafult r mood only:-------------------------")

#By default read a file , mood is "r":
d = open("esd")
print(d.read())


print("-------------------------At a time read and write with w+ mood:-------------------------")

#At a time write and read a file with w+ mood:
d1 = open("apurba.txt","w+")
print(d1.write("Apurba is my name."))

d1 = open("apurba.txt","w+")
print(d1.read())

print("-------------------------At a time read and write with a+ mood:-------------------------")
#At a time write and read a file with a+ mood:
#Note: same file object variable should be taken:
d2 = open("shuvra","a+")
print(d2.write("Apurba is my name."))
print(d2.write("My father name is Ranjit Chandra Debnath.."))
print(d2.write("My father name is Ranjit Chandra Debnath.."))
print(d2.write("New line added"))

#Duplicate creation will be ignored for reading file content by a+ mood:

d2 = open("shuvra","a+")
print(d2.read())

