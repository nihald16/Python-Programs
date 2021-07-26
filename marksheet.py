a=int(input("Enter marks of s1="))
b=int(input("Enter marks of s2="))
c=int(input("Enter marks of s3="))
d=int(input("Enter marks of s4="))
e=int(input("Enter marks of s5="))

if a>=40 and b>=40 and c>=40 and d>=40 and e>=40 :
    print("Pass")
else:
    print("Fail")

sum=a+b+c+d+e
avg=(sum)/5

print("Sum =",sum ,"\nAverage=",avg)