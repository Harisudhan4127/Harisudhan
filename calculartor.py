def add(a,b):
    print(a+b)
    return a+b 
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

num1 = int(input("Enter the no1 : "))
num2 = int(input("Enter the no2 : "))

print("1. add\n2. sub\n3. multi\n4. div")
option = int(input("Enter the option : "))

if option == 1:
    print(add(num1,num2))
elif option ==2 :
    print(sub(num1,num2))
elif option ==3:
    print(mul(num1,num2))
elif option ==4:
    print(div(num1,num2))
else:
    print("Erro : incorrect option")