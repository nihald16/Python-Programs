n=int(input("enter no of student:"))
dict1={}
list1=[]

for i in range(0,n):
    name=input("enter name :")
    #mark=input("enter marks:").split()
    list1=list(input().split())
    dict1[name]=list1

query=input("enter name of student:")
avg=0.0
for n,v in dict1.items():
    if query==n:
        for i in v:
            avg=avg+float(i)

        l=len(v)

        avg=avg/l
        print("{:.2f}".format(avg))
    