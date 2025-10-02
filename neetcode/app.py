name=input("What is your name: ")

userChoose=input("Dear "+name+ "Do you want play the game: ")

if userChoose =="yes":
    print("Let's play the game ")
    direction =input("please enter the direction please: ").lower()
    if("Where do you want go left or right (left/right) "):
        if direction=="left":
            print("You are die:")
        elif direction=="right":
            print("You are passed the way")
        else:
            print("wrong attempet")


