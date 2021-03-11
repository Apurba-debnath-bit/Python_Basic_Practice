import time
#time.sleep()
initial = time.time()
print(initial)
i = 1
# while i <= 46:
#     print(i, "This is Apurba")
#     i += 10
while i <= 488:
    print(i, "This is Apurba")
    time.sleep(2)
    i += 3
stopped_while = time.time()
print(stopped_while)

print("while loop ends at: ", (stopped_while - initial), "seconds")

print()

print("for loop: \n")
initial2 = time.time()

for i in range(1, 468, 2):
    print(i, " This is Apurba ")

stopped_time = time.time()
print("for loop ends at: ", stopped_time - initial2, "seconds")

lcaltime = time.asctime(time.localtime(time.time()))
print(lcaltime)
