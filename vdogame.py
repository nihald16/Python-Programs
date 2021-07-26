class oprators:

    tuple1 = ("Arithmetic","comparison")
    t1 = ('+',"*","-",'/','//','%','**')
    t2 = ("==","!=","<=",">=","<",">")
    op=[t1,t2]
    a = int(input("enter first  number : "))
    b = int(input("enter second number : "))
    
  
    print("Your value are store in the variable a and b")

    print("a = ",a)
    print("b = ",b)

    print("Datatype of variables are : ")
    print("a = ",type(a))
    print("b = ",type(b))

    x=0
    for i in tuple1:
        print("\t\t",x,":",i)
        x+=1

    n=int(input("chosse number :"))

    
class operation(oprators):
    def display(self):
        x=0 
        for i in self.op[self.n]:
            print("\t\t",x,":",i)
            x+=1

    def arithmatic(self):
        self.display()
        self.m=int(input("choose number :"))
        self.result=(
        self.a+self.b,
        self.a*self.b,
        self.a-self.b,
        self.a/self.b,
        self.a//self.b,
        self.a//self.b,
        self.a**self.b)

    def comparision(self):
        self.display()
        self.m=int(input("choose number :"))
        self.result=(
        self.a==self.b,
        self.a!=self.b,
        self.a<=self.b,
        self.a>=self.b,
        self.a<self.b,
        self.a>self.b)

    
class run(operation,oprators):
    def run(self):
        if self.n==0:
            self.arithmatic()
        elif self.n==1:
            self.comparision()
        else:
            print("choose correct option :")

        for j in range(0,7):
            if self.m==j:
                print("result =",self.result[j])
 

obj=run()
obj.run()
   
        
'''a = int(input("enter first  number : "))
b = int(input("enter second number : "))
print("Your value are store in the variable a and b")

print("a = ",a)
print("b = ",b)

print("Datatype of variables are : ")

print("a = ",type(a))
print("b = ",type(b))

print("select any option to perform operation : ")

tuple1 = ("Arithmetic","comparison","Assignment","Bitwise","Logical")
t1 = ('+',"*","-",'/','//','%','**')
t2 = ("==","!=","<=",">=","<",">")
t3 = ("=","+=","-=","*=","%=","**=","/=")
t4 = ("&","|","<<",">>","~")
t5 = ("and","or","not")
op = (t1,t2,t3,t4,t5)

x=1
for i in tuple1:
    print("\t\t",x,":",i)
    x+=1

n = int(input("Choose operator : "))


y=z=1
for j in tuple1:
    if n is y:
        print("you choose",j,"operator")
        for j in op[n-1]:
            print("\t\t",z,":",j)
            z+=1
    y+=1

n = int(input("choose operation :"))

def Arithmetic():
    add=a+b
    mul=a*b
    sub=a-b
    div=a/b
    fdiv=a//b
    module=a%b
    power=a**b
    return add,mul,sub,div,fdiv,module,power

print("result :\n")
for i in range(1,n):
    for j in Arithmetic():
        if i==n:
            print(j)
            break
    print(j)'''
        



