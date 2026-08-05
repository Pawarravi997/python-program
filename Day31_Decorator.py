'''
>A decorator in python is a design pattern and a higher order function that modifies or exyended the behaviour of an existing function,method, or


>reduce
>recursive
>pure function
>impure function
'''


#ex1:
# def extra(fun):
#     def inner():
#         fun()
#         print('ravii')
#     return inner

# @extra
# def printer():
#     print('ravii')
#     print('ravii')
# printer()    


# def square(fun):
#     def inner():
#         result=fun()
#         sq=result**2
#         return sq
#     return inner()


# @square
# def add():
#     n1=int(input('n1:'))
#     n2=int(input('n2:'))
#     sum=n1+n2
#     return sum


#ex1:
# def title_case(fun):
#     def inner():
#         result=fun()
#         r=result.title()
#         return r
#     return inner

# def full_name():
#     fn=input('fn:')
#     mn=input('mn:')
#     ln=input('ln:')
#     fname=f'{fn} {mn} {ln}'
#     return fname

# full_name=title_case(full_name)
# print(full_name())

#---------or---------------

# def title_case(fun):
#     def inner():
#         result=fun()
#         r=result.title()
#         return r
#     return inner

# @title_case
# def full_name():
#     fn=input('fn:')
#     mn=input('mn:')
#     ln=input('ln:')
#     fname=f'{fn} {mn} {ln}'
#     return fname
# print(full_name())



#ex2:


# def title_case(fun):
#     def inner(fn,mn,ln):
#         result=fun(fn,mn,ln)
#         return result
#     return inner

# @title_case
# def full_name(name,mname,lname):
#     fname=f'{name} {mname} {lname}'
#     return fname

# print(full_name('aaa','bbb','ccc'))



# #ex3:

# def login(fun):
#     def inner():
#         username=input('username:')
#         password=input('password:')
#         if username=='ravi' and password=='1234':
#             fun()
#         else:
#             print('invalid details')   
#     return inner

# @login
# def attandance():
#     print('welcome to attandance page ')

# @login
# def livebatch():
#     print('welcome to livebatch page ')

# @login
# def testreport():
#     print('welcome to testreport page ')    


# attandance()    
# livebatch()
# testreport()