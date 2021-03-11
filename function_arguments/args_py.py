#One normal function :
def func(ab, ac, cb,s):
    print(ab,ac, cb,s)


func(44,56,67,s="arg")




#convention is : order must be(normal, *args, **kwargs)
def function_arg(normal,*arg,**kwargs):
    print("Normal: {0}".format(normal))
    for item in arg:
        print(item)
    print("all kwarg is here: \n")
    for key, value in kwargs.items():
        print(f"{key} is  a {value}")



arg = ["Sagor", "Puja", "Rathi","Shuvra"]
kwargs ={"Sagor":"Cooker", "Rahim":"Player","Puja":"Dreamer"}
function_arg(3,*arg,**kwargs)

