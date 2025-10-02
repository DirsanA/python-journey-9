
user_choose=input("please enter your choice view for view password and add for adding password (view/add): ")

def add():
    name=input("Account Name: ")
    pwd =input("Account Password: ")
    with open('password.txt','a') as f: 
        # with will do to close the file automaticaly
        f.write(name+"|"+pwd+"\n" )
        
def view():
    pass

while True:
    if user_choose=="view":
       view()
    elif user_choose=="add":
         add()
    elif user_choose=="quit" or "q":
        break
    else:
        continue
    