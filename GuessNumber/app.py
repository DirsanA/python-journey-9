
import random

target_number=random.randint(1,100)
def guess_number():
    while True:
        try:
            guess_number=int(input("please enter the number between 1 and 100: "))
            if guess_number<1 or guess_number>100:
                print("please enter the number between 1 and 100: ")
            elif guess_number==target_number:
                print("Congratulation You have succesfuly got the number ",guess_number)
                break
            elif guess_number<target_number:
                print("It is smaller number that you enter: ")
            elif guess_number>target_number:
                print("It is greater number you enter: ")
        except ValueError:
            print("Please enter correct number: ")
guess_number()

