#FIBNOCCI SERIES
def fibnocci(number):
    n1,n2=0,1
    for i in range(number):
        print(n1)
        sum=n1+n2
        n1=n2
        n2=sum
    

fibnocci(10)



