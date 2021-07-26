#WAP A PROGRAM TO ACCEPT FIVE NUMBERS AND FIND BIGGEST NUMBER 
n1=int(input("enter 1st number:"))
n2=int(input("enter 2nd number:"))
n3=int(input("enter 3rd number:"))
n4=int(input("enter 4th number:"))
n5=int(input("enter 5th number:"))

#finding greater number
#by using function
list1=[n1,n2,n3,n4,n5]
m=max(list1)
print(m,"is greater number ")

#by using nested if

if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    print(n1,"is greater number")
elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print(n2,"is greater number ")
elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print(n3,"is greater number ")
elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
    print(n4,"is grater number")
else:
    print(n5,"is grater numbber")



