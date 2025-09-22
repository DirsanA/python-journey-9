
print("Do you want play the game: ")
userResponse =input().lower()
if userResponse!= "yes":
    quit()
else:
    print("CPU stands for:")
    answer=input().lower()
    if answer=="centeral processing unit":
        print("correct")
    else:
        print("Incorrect")
print("GPU stands for:")
answer=input().lower()
if answer=='graphics processing unit':
    print("correct")
else:
    print("Incorrect")

    