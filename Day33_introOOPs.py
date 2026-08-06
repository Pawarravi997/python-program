# class Student:
#     def __init__(self): #first parameter of init funtion is self
#         print('hello myself init funtion, which excute after the __new__ function. dont need to call they will auto execute when you create a object.it runs for all objects')
#     def m1(self):
#         print('this is a m1 function ')    

# s1=Student()
# s2=Student()
# s3=Student()
# s4=Student()
# s1.m1()        

#--------interview question.
#init function
#new function
#self
#constructor in py
#diff betwwn ne and init
#what happen if you dont define constructor in the class
#can a constructor return a value? why or why not?



#__new__ is a special method that is responsible for creating a new object.

# class Student:
#     def __init__(self):
#         print(f'id of the self is {id(self)}')

# s1=Student()
# print(f'id of the s1 is {id(s1)}')
# print('---'*20)

# s2=Student()
# print(f'id of the s2 is {id(s2)}')
# print('---'*20)

# s3=Student()
# print(f'id of the s3 is {id(s3)}')


# class Bank_account:
#     def __init__(self):
#         print(f'id of the self is {id(self)}')
# s1=Bank_account()
# print(f'id of s1 {id(s1)}')        

#------use any parameter name instead of the self
# class Bank_account:
#     def __init__(n1): 
#         print(f'id of the self is {id(n1)}')
# s1=Bank_account()
# print(f'id of s1 {id(s1)}')        


# class Employee:
#     def __new__(cls):
#         print('new method')
#         obj=super().__new__(cls)
#         return obj
#     def __init__(self):
#         print('Init method')

# s1=Employee()        




# class Student:
#     def __init__(self):
#         # self.name=name
#         print('welcome')

# s1=Student()        


# class Employee:
#     def __new__(cls):
#         print('hello')
#         obj=super().__new__(cls)  #new return not init    
#         return obj
#     def __init__(self):
#         print('init function') 
# s1=Employee()
