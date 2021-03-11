#filter function 

list1 = [2,3,4,5,6,7,8,9,10]
def greter_than_5(num):
    return num > 5#this func return true, if num > 5
value = list(filter(greter_than_5,list1))
print(value)

