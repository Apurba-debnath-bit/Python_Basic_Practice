while 1:
    user = input("Enter your name: ")
    print(f"\n{user} says: Hello Python! Do you know i love you ")

    inputlist1 = ["yes", "no", "not"]

    inputfirst1 = input("Python, Answer me please:(yes or no): ")

    if inputlist1[0].upper() == inputfirst1.upper():
        print(f"{user} says: I love you too..")
        break
    elif inputlist1[1].upper() == inputfirst1.upper():
        print(f"{user} says: I don't love you also ")
        break
    elif inputlist1[2].upper() == inputfirst1.upper():
        print(f"{user} says: Really, I don't love you also ")
        break
    else:
        print(f"{user} says: Don't know what are you saying about...Plz say again..")


while 1:
    apu = user
    inp = input("Enter user name:   ")

    if apu == inp:
        print("Username correct.")
        break
    else:
        print("Wrong input!..")




while 1:
    pass1 = "1234"
    input3 = input("Enter your password: ")
    if pass1 == input3:
        print("Successfully Login..")
        break
    else:
        print("Wrong password")

print(f"-----------Login as {apu} Debnath.-------------------")