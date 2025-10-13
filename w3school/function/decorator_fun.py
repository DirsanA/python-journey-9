# def dec_fun(fun):
#     def myInner():
#         return fun().upper()
#     return myInner


# @dec_fun
# def say_hello():
#     return "hello"

# print(say_hello())


user={
    "username":"Dirsan",
    "acess_level":"admin"
}

def user_has_permssion(func):
    def secure_my_func():
        if user.get('acess_level')=="admin":
            return func()
        else:
            print("You dont have acess!")
    return secure_my_func 

@user_has_permssion
def myfunction():
    return 'admin has acess password'

print(myfunction())