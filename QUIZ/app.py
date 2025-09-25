
print("Do you want play the game: ")
userResponse =input().lower()
userResult =0
if userResponse!= "yes":
    quit()
else:
    print("CPU stands for:")
    answer=input().lower()
    if answer=="centeral processing unit":
        userResult=userResult+1
print("GPU stands for:")
answer=input().lower()
if answer=='graphics processing unit':
    userResult=userResult+1


calculateTotalResult=(userResult/2) * 100

print("You have got ",str(userResult )+"%")

