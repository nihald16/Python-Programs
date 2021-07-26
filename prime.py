'''def check(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return True
            
                
x=check(9)
if x:
    print("given number is not prime")
else:
    print("given number is prime ")'''
	

def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else: 
        return False 

sequence = ['g', 'e', 'e', 'i', 'k', 's', 'p', 'r'] 

filtered = filter(fun, sequence)
print('The filtered letters are:') 
for s in filtered:
    print(s)