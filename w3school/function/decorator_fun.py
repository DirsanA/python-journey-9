def dec_fun(fun):
    def myInner():
        return fun().upper()
    return myInner


@dec_fun
def say_hello():
    return "hello"

print(say_hello())