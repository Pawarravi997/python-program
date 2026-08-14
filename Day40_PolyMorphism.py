#------PolyMorphism:
'''
>The word "polymorphism" means "many forms"  
>In programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

1.Method Overloading
Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures.
Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note: Python does not support method overloading. We may overload the methods but can only use the latest defined method.

2.Method Overriding
Method overriding is an example of run time polymorphism. In this, the specific implementation of the method that is already provided by the parent class is provided by the child class. 
It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding. In method overriding, inheritance always required as it is done between parent class(superclass) and child class(child class) methods

'''

# class book:
#     def __init__(self,bn,pr,pg):
#         self.book_name=bn
#         self.price=pr
#         self.page=pg

#     def __add__(self, other):
#         return self.price + other.price    

# b1=book('pyhton',1000,150)
# b2=book('java',1500,100)   
# print(b1+b2)



# class Hotel:
#     def __init__(self,hn,rate):
#         self.hotel_name=hn
#         self.rate=rate

#     def __gt__(self, other):
#         if self.rate>other.rate:
#             print(f'yes,{self.hotel_name} is expensive than {other.hotel_name}') 
#         else:
#             print(f'No, {other.hotel_name} is expensive than {self.hotel_name}')
# h1=Hotel('tiranga hotel',2000)
# h2=Hotel('taj totel',5000)    




#overloading : here parent class will be modified in the child class as per requirement with the same method name but different behaviour
# class A:
#     def m1(self):
#         print('hii, i am m1 method')
#     def m2(self):
#         print('hii, i am m2 method')
#     def m3(self):
#         print('hii, i am m3 method of A class')

# class B(A):        
#     def m3(self):
#         print('hii, i am m3 method of B class')         

# b1=B()
# b1.m3()                


#ex of overrriding


















   





























