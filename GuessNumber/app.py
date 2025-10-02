import random

def randum_num():
    num=random.randint(1,100)
    while True:
        random_input=input("Please Enter number between 1 and 100: ")
        if num!=random_input:
            if num>random_input:
                print("It is greater number you enter : ")
            elif num<random_input:
                print("It is smaller number that you enter: ")
        else:
            print("Congratulation You have succesfuly got the number ",num)
        
randum_num()