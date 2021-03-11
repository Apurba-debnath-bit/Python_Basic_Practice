def myfunc(func):
    def execute():
        print("Execute Now: ")
        func()
        print("done")
    return execute

@myfunc
def who_is_apurba():
    print("I am apurba ")

#who_is_apurba = myfunc(who_is_apurba)

who_is_apurba()#now this is decorator function


