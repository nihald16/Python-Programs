#find largest and second largest number

#in list
n = int(input())
list1=[] 
for i in range(0,n):
    list1.append(int(input()))    
   
print(list1)
mx=max(list1)
print("maximum no=",mx)
smx=min(list1)
print("default minimum value=",smx)

for i in range(0,n):
    if list1[i]>smx and mx != list1[i]:
        smx=list1[i]
       
print("second maximum no=",smx)

