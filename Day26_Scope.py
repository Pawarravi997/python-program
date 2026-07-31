#-----Scopes
'''
their are two types of a scope in the phython

1.global scope which is define outside a function
>variable which is defined in the global scope is called as a global variable

2.local scope which is define space inside a function
>variable which is defined in the local scope is called as a local variable



ex:

#global scope
x=100
y=200
def fun():
    #local scope
    a=11
    b=12
    print(a,b) #we can acess local varible within local scope
    print(x,y) #we can acess globle varible within local scope
fun()    

#Global variable---> x & y
#Local variable---> a & b

'''

#The global keyword is used when you want to modify (change) a global variable inside a function.
#Global tells Python that a variable inside the function refers to the global variable, not a new local variable. 


#ex1:
# x=100
# y=200
# def fun():
#     a=11
#     b=12
#     print(a) 
#     print(x)
#     global y
#     y=y+20
#     print(y)
# fun()     
# print(y)


'''
>we can used globle and local variable within a local scope but we cant modify varible within a function.
>if you want to use the varible outside a function at that time we can use the return statement.return statement return to that caller thats why we can assign a varible to that function . return help us to use the varible outside the function.
>whenever we used the return statement .this varible is goes to the caller and at that time we can assign the varible name to that caller and print them or used them outside the function
'''
# #ex:
# x=100
# def fun(n1,n2):
#     global x
#     add=n1+n2
#     return add
# x=fun(10,20) 
# print(x)
   


#-----Nested function

#ex1:
# def f1():
#     print('welcome to the f1()')
#     def f2():
#         print('welcome to the f2()')
#     return f2    
# f2=f1()
# f2()        


#ex2:
# def f1():
#     print('Ravii')
#     def f2():
#         print('Pawar')
#     return f2    
# name=f1()
# name()        

# #ex3:
# def num1():
#     n1=10
#     def num2():
#         n2=20 
#         return n2 
#     return n1,num2
# n1,num2=num1()
# n2=num2()
# print(n1+n2)

# #ex4:
# def fname():
#     fn='ravii'
#     def lname():
#         ln='pawar'
#         return ln 
#     return fn,lname
# fn,lname=fname()
# ln=lname()
# print(fn+' '+ln)

# #ex4:
# def square(num):
#     sqr=num**2
#     def cube(num):
#         cb=num**3
#         return cb
#     return sqr,cube
# sqr,cube=square(3) 
# cb=cube(3) 
# print(sqr+cb)

# #ex5:
# def f1(n1):
#     r1=n1/2
#     def f2(n2):
#         r2=n2/2
#         def f3(n3):
#             r3=n3/2
#             return r3
#         return r2,f3
#     return r1,f2
# r1,f2=f1(10)
# r2,f3=f2(20)
# r3=f3(30)
# print(r1+r2+r3)