#---Flow Control Statement

#---conditional statement
# 1.if statement
# 2.else statement
# 3.if else statement

#---if statement
#ex1:
# password=input('enter password:')
# if password=='12345':
#     print('succesfully login')
# print('thank you ')    

#ex2:
# username=input('enter username:')
# password=input('enter password:')
# if username =='ravi' and password=='12345' :
#     print('succesfully login')
# print('thank you ')  

#ex3:
# numbers=[10,20,30,40,50,60,70,80,90]
# for num in numbers:
#     if num>=50:
#         print(num)


#ex4:
#wap to iterate only even numbers from given list
# numbers=[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num % 2==0:
#         print(num)


#ex5:
#wap to iterate only negative numbers on list
# numbers=[1,2,-3,4,5,-6,7,8,9,-10]
# for num in numbers:
#     if num<0:
#         print(num)

#ex6:
#wap to print sum of all odd numbers
# numbers=[11,12,13,14,15,16,17,18,19,20]
# sum=0
# for num in numbers:
#     if num % 2!=0:
#         sum=sum+num
# print(f'total sum of all odd number is:{sum}')

#ex7:
#wap to iterate only those name startwith 'v'
# name=['vijay','virat','ravi','raja','ved']
# for nm in name:
#     if nm[0]=='v':
#        print(nm)

#wap to iterate only those name startwith 'v' and 'V'        
# name=['vijay','virat','ravi','raja','ved']
# for nm in name:
#     if nm.startswith('v'):
#        print(nm)

# #wap to iterate only those name startwith 'v' and 'V'
# name=['vijay','virat','ravi','raja','Ved']
# for nm in name:
#     if nm.startswith('v') or nm.startswith('V'):
#        print(nm)       
        
# #wap to iterate only those name startwith 'v' and 'V'
# name=['vijay','virat','ravi','raja','Ved']
# for nm in name:
#     if nm[0]=='v' or nm[0]== 'V':
#        print(nm)
        
# name=['vijay','virat','ravi','raja','Ved']
# for nm in name:
#     if nm.lower()[0]=='v':
#         print(nm)


#---if else statement

#ex1:
# age=eval(input('enter your age:'))
# if age >=18:
#     print('you can vote')
# else:
#     print('not eligible for vote')    

#ex2:
# num=int(input('enter number:'))
# if num%2==0:
#     print('number is even')
# else:
#     print('number is odd')    

#ex3:
#wap to print even numbers and odd numbers in two different lists.
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# for num in numbers:
#     if num % 2==0:
#         even.append(num)  
#     else:
#         odd.append(num)    
# print(f'list of even numbers is :{even}')
# print(f'list of odd numbers is :{odd}')      

#ex4:
#wap to print sum of all even numbers and odd numbers.
# numbers=[1,2,3,4,5,6,7,8,9,10]

# even_sum=0
# odd_sum=0       
# for num in numbers:
#     if num % 2==0:
#         even_sum=even_sum+num    
#     else:
#         odd_sum=odd_sum+num
# print(f'list of addition of all even numbers is :{even_sum}')
# print(f'list of addition of all odd numbers is :{odd_sum}')     

