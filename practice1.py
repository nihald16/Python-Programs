'''print("*"*30)

for i in range(5):
    print("number :",i)
    print("adress of number:",id(i))

if i==1:
    print("i catch number")


a=10
print(a,"address",id(a))

if a==10:
    print("true")


print("number :",a,"address",id(a))

if a==10:
    a=a+1
    print(a,"address",id(a))

print("number :",a,"address",id(a))'''


n=int(input())
list1=[]

for i in range(0,n):
    query=input().split()

    if 'insert' in query:
        list1.insert(int(query[1]),int(query[2]))
    elif 'append' in query:
        list1.append(int(query[1]))
    elif 'print' in query:
        print(list1)
    elif 'remove' in query:
        list1.remove(int(query[1]))
    elif 'sort' in query:
        list1.sort()
    elif 'pop' in query:
        list1.pop()
    elif 'delete' in query:
        list1.__delitem__(int(query[1]))
    elif 'reverse' in query:
        list1.reverse()
    else:
        print("not working")

    