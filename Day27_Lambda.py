#-------------Lambda Function
'''
>lambda function is a single line function
>used for simple operation
>used the lambda keyword fro define the lambda function
>lambda is a small,anonymous function that is defined without a name.
>anonymous:they dont have a name unless you assign them to a varible.(ex3)
>In lambda function we have provide multiple parameter but only one expression will be perform.if you have get multiple expression form the lambda function we have written in the list,set and tuple (ex4)
>A lambda function in Python is a small, anonymous function that is defined without a name and contains only a single expression. Unlike standard functions declared with the def keyword, lambda functions are written inline using the lambda keyword and automatically return the result of their expression without requiring an explicit return statement
syntax:
       lambda parameter:expression
       
'''
#ex1:
# def square(num):
#     sqr=num**2
#     return sqr
# print(square(6)) 
# print((lambda num:num**2) (5))  #using the lambda function

#ex2:
# def add(n1,n2):
#     sum=n1+n2
#     return sum
# print(add(10,20))
# print((lambda n1,n2:n1+n2)(10,20)) #using the lambda function


#ex3:
# f_name=lambda fn,mn,ln:f'{fn} {mn} {ln}'   # if you have assign a name to the function they have not anonymous anymore 
# print(f_name('cockroach','janata','party'))

#ex4:
# calci=lambda n1,n2:(n1+n2,n1-n2,n1*n2,n1/n2)
# print(calci(100,20))


#ex5:
# cube=lambda num : num**3
# print(cube(5))
# print((lambda num : num**3)(5))


#ex6:
# check=(lambda num: 'even' if num%2==0 else 'odd' )
# print(check(65))



