#The python map() function is used to return a list of results 
# after applying a given function to each item of an iterable(list, tuple etc.)
#function- It is a function in which a map passes each item of the iterable.
#iterables- It is a sequence, collection or an iterator object which is to be mapped.
#example:
# list1=[1,2,3,4,5,6,7,8,9,10]
#if we want type of object of given list int to str 
# print(type(list1[0]))
# list1=list(map(str,list1))
# print(type(list1))
# print(type(list1[0]))

#if we want to find square of number present in list
# def sqr(x):
#     return x*x
# list2=[]
# for i in list1:
#     list2.append(sqr(i))
 

# #with map function

# list1=list(map(sqr,list1))
# print(list1)

# #with lamada

# list1=list(map(lambda x:x*x,list1))
# print(list1)

# n=int(input())
# integer=map(int,input().split())

# t=tuple(integer)
# print(t)

list1=[1,2,3,4,5,6,7,8,9,10]

def greater(num):
    return num>5

maps=list(map(lambda x:x%2==1,list1))
print(maps)

filters=list(filter(lambda x:x%2==1,list1))
print(filters)




    


