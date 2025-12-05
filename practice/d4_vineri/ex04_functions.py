# functions

def func(*args):
    print(args)

func("a", "b", "c")

def func(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

func("a", "b", "c")


t = (1, 5, 7)

func("a", t)
func("a", *t)



def func(arg1, arg2, *args, kwarg1="default 1", kwarg2="default 2"):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)

func("ala", "bala", "porto", "cala")

def func(arg1, arg2, kwarg1="default 1", kwarg2="default 2"):
    print(arg1)
    print(arg2)
    #print(args)
    print(kwarg1)
    print(kwarg2)

func("ala", "bala", "porto", "cala")


def func(arg1, arg2, *args,
         kwarg1="ceva", kwarg2="default 2", **kwargs):
    print(arg1)
    print(arg2)
    print(args)   # <-- listă

    print(kwarg1)
    print(kwarg2)
    print(kwargs) # <-- dicționar


func("ala", "bala", "porto", "cala",
     kwarg1="altceva", another="interesant", andanother="wow!")


# Exemplu
def caller(callback, *args, **kwargs):
    print("îl rulez pe caller")

    return callback(*args, **kwargs)


def myfunc(a, b, mydefault="ceva"):
    print(a, b, mydefault)


caller(myfunc, 15, 20, mydefault="altceva")

