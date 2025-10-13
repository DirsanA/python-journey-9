print("What you want do: (r/w)")

def read_data():
    with open("index.txt","r") as f:
        lines=f.readlines()
        for i in lines:
            print(i)
            
def write_data():
    user_data=input("please enter you data: ")
    with open("index.txt","a",) as f:
        f.write(user_data)
         
while True:
    user_choose=input("please enter your choose: ")
    
    if user_choose=="r":
        read_data()
    if user_choose=="w":
        write_data()