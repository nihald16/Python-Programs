#finding student with less marks in class by using dictonary

n=int(input("enter the total number of student:"))

dict1={}
for i in range(0,n):
    name=input("enter name =")
    score=float(input("enter percentage="))
    dict1[name]=score
print()  

smx=min(dict1.values())

print("less percentage =",smx)
print("student who have less percentage :",end="")

for x,y in dict1.items():
   if y==smx :
       print(x,end=" ")
print()