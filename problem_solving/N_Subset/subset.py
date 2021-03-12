num = int(input("Enter the number of set member: "))

parent = num + 2

child = 0

for i in range(1,num):
    #print(i)
    child = child + i
     
#print("count is: ", child)
total =(parent+child)
print("The number of sub set will be: ", total)

    


