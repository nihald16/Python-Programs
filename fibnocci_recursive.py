print("fibnocci without recursive function :")

def fibnocci1(number):
    n1,n2=0,1
    for i in range(number):
        print(n1)
        sum=n1+n2
        n1=n2
        n2=sum
fibnocci1(10)

print("-"*20)
print("fibnocci series with recursive function :")

def fibnocci(n,n1=0,n2=1):
    if n==0:
        exit()
    else:
        print(n1)
        sum=n1+n2
        n1=n2
        n2=sum
        fibnocci(n-1,n1,n2)

fibnocci(10)

