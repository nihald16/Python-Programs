#Get a list of name as an input from the user and make 
# the first letters in caps and print each word as a list

name=input("enter name :")

lst=[]

for i in name:
    lst.append(i)
    if lst[0] >='a' and lst[0]<='z':
        lst[0]=lst[0].upper()
    

print(lst)


