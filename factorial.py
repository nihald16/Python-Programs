#FACTORIAL NUMBER
def factorial(num=1):
    facto=1
    if num<0:
        print("fatorial not exist dor negative numbers")
    elif num==0:
        print("0 is 1")
    else:
        for i in range(1,num+1):
            facto=facto*i
        print(f"factorial of number {num} is :",facto)

factorial(5)