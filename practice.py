j=input()
s=input()
list1=[]

for stone in s:
    for i in j:
        if i==stone:
            list1.append(stone)
print(list1)
print(len(list1))


