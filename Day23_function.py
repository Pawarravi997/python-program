#-----------function
'''
function is a resuable block of code

1.function defination
def function_name():
    #block
    #code
2.function calling
function_name() 
    
'''
#ex1:

# #wap to create a factorial funtion
# def factorial():
#     number=int(input('enter a num:'))
#     fact=1
#     for num in range(1,number+1):
#         fact=fact*num
#     print(f'factorial of {num} is {fact}')

# factorial()        


#ex2:

# #wap to print square of that number
# def square():
#     number=int(input('enter number:'))
#     sqr=number**2
#     print(f'square of {number} is {sqr}')   
# square()     


#ex3:

#wap to for armstrong number
# num = int(input('enter a number:'))
# snum=str(num) # used to convert into string bz we cannot iterate int thats why convert into str to check the length
# n=len(snum)
# sum=0
# for i in snum:
#     sum=sum+int(i)**2 #here convert i into int bz str has not pow() function
#     # print(sum)
# if num==sum:
#     print('armstrong number')
# else:
#     print('not armstrong number')        


#ex4:

# def armstrong():
#     num = int(input('enter a number:'))
#     snum=str(num) 
#     n=len(snum)
#     sum=0
#     for i in snum:
#         sum=sum+int(i)**2 
#     if num==sum:
#         print('armstrong number')
#     else:
#         print('not armstrong number')        
# armstrong()        



#ex5:
#-----parameter and argument

#wap to use parameter and argument instead of input and value function

# def sum(num1,num2):
#     result=num1+num2
#     print(result)

# sum(100,20)


#ex6:
# def armstrong(num):
#     snum=str(num) 
#     n=len(snum)
#     sum=0
#     for i in snum:
#         sum=sum+int(i)**2 
#     if num==sum:
#         print('armstrong number')
#     else:
#         print('not armstrong number')        
# armstrong(153)       


#ex6:

# def create_email(fn,ln,cn):
#     email=f'{fn}_{ln}@{cn}.com'
#     print(email)
# create_email('ravi','pawar','tcs')   



#ex7:

#wap to create a function to check number is perfect or not


# def per_num(num):
#     sum=0
#     for i in range(1,num):
#         # print(i)
#         if num%i==0:
#             # print(i)
#             sum=sum+i
#     if sum==num:
#         print("yes")
#     else:
#          print("no")

# per_num(60)

# numbers = [10,20,30,40,50]
# for num in numbers:
#     if num%2==0:
#         print('even number')
#     else:
#         print('odd number')    
#         #using for loop we can iterate all number from the numbers list and then useing if condition check condition and get even nubers



#----parameter
'''
a parameter is a varible in the function definition that act as  a placeholder for the value that will be passed to the function when it is called.parameter define what kind of data the function expects.

syntax:
       def function_name(para1,para2.....):  #function define
           #block of code

'''

#----Argunment
'''
an argunment is the actual value or data that you pass to the function when calling it.the argunment are asssigned to the cporresponding parameter in the function

syntax:
       function_name(arg1,arg2......):  # function calling
           #block of code


'''

#Write a function that takes a list of numbers and returns a new list containing only the even numbers.
def get_even_numbers(num):
    new_list = []
    for i in num:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

num = [1,2,3,4,5,6,7,8,9,10]
result = get_even_numbers(num)
print(result)