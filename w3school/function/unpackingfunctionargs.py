def sum_args(*args):
    total=0
    for i in args:
        total=total+i
    
    print(total)
        
list_num=[56,67,68,69]

sum_args(*list_num)