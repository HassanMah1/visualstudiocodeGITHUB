from tokenize import Double

def add(num1:Double,num2:Double):
    result=num1+num2
    print(result)
def sub(num1:Double,num2:Double):
    result=num1-num2
    print(result)
def divide(num1:Double,num2:Double):
    result=num1/num2
    print(result)
def multi(num1:Double,num2:Double):
    result=num1*num2
    print(result)


num1=int(input("enter number 1 "))
op=(input("enter op"))
num2=int(input("enter number 2 "))

if op=="+":
    add(num1,num2)
elif op=="-":
    sub(num1,num2)
elif op=="/":
    divide(num1,num2)
elif op=="*":
    multi(num1,num2)
else:
    print('invalid opeŉrator ssss')



