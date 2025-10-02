def sum(operand1,operand2):
     sumNumber= operand1+operand2
     return sumNumber
def mul(operand1,operand2):
    mulNumber=operand2*operand1
    return mulNumber
def div(operand1,operand2):
    divNumber=operand1/operand2
    return divNumber
def sub(operand1,operand2):
    subNumber=operand1-operand2
    return subNumber

print("Welcome to My app: ")
num1 = int(input("please enter the first  number: "))
num2 = int(input("please enter the second  number: "))

print ("________________________________")
print("Please choose what you want do ")
print("1.SUM")
print("2.SUB")
print("3.MUL")
print("4.DIV")
print ("________________________________")

choose = input("please enter your choose: ")
if choose == "1":
        result = sum(num1,num2)
        print("The result of the number is: " + str(result))
elif choose == "2":
        result = sub(num1,num2)
        print("The result of the number is: " + str(result))
elif choose == "3":
        result = mul(num1,num2)
        print("The result of the number is: " + str(result))
elif choose == "4":
        result = div(num1,num2)
        print("The result of the number is: " + str(result))
else:
    print("please enter correct choose: ")
    
