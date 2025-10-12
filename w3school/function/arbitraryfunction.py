
#  arbitrary function it is function that is when we do not know 
# the actual argument that is passed to the function

def num(*args):
    for i in args:
        print(i)


num(1,2,3,4,5)