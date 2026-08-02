#------------Higher order function
'''
>A Higher-Order Function (HOF) is a function that works with other functions. It can accept a function as an argument, return a function or do both. This allows functions to be reused and combined in flexible ways.
>The filter() function in Python is a built-in function used to extract elements from an iterable (like a list, tuple, or set) that satisfy a specific condition. It evaluates each item against a testing function and only keeps the items that return
>when used lambda funtioon inside the filter we can only one parameter is used


Filter(function,iterable)
'''
#ex1:
# number=[1,2,3,-4,5,6,-7,8,9,-9,10]
# def ispositive (num):
#     if num>0:
#         return True
#     else:
#         return False
# print(list(filter(ispositive,number)))    

#ex2:
# number=[10,20,30,50,40,30,70]
# def isgreater(num):
#     if num>30:
#         return True
#     else:
#         return False
# print(tuple(filter(isgreater,number)))    
# print(set(filter(isgreater,number)))   
# print(list(filter(isgreater,number)))     

# # ex3:
# number= [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda num:num%2==0, number)))

#ex4:
# student=['ravi','raju','virat','modi','jadu']
# print(tuple(filter(lambda name:name[0]=='r',student)))
# print(list(filter(lambda name:name[0]=='r',student)))
# print(set(filter(lambda name:name[0]=='r',student)))


#ex5:
#wap which is dividible by 3 and 5
# number=[10,20,30,44,50,60,70,80,90,101]
# print(list(filter(lambda num:num%3==0 and num%5==0,number)))


#ex6:
# number= [10,22,63,84,35,96,79,85,93,110]
# print(list(filter(lambda num: num%2!=0,number)))


#ex7:
# number= [10,22,63,84,35,96,79,85,93,110]
# print(list(filter(lambda num : num%2==0 and num%3==0 ,number)))


#ex8:
