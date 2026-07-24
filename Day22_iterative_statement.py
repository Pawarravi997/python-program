
#--range

# products={}

# for i in range(3):
#     p_name=input('enter product name:')
#     p_price=eval(input('enter product price:'))
#     products[p_name]=p_price
# print(products)    

# for loop is a looping statement it is used to execute a block of code repetedely for each items in a sequence like list,tuple,dict,set and range


#---------while loop
'''
while loop is a looping statement in python,it is used to execute a block of code repedetly as long as the given condition is true.until the given condition becomes false
'''

# num=1  #initilize
# while num<5:  # condition
#     print('Ravii Pawar')
#     num=num+1 #update  


#ex1:
# att=[]
# add='yes'  #initilize
# while add =='yes':  #condition
#     name=input('enter name:')
#     att.append(name)
#     add=input('do you want to add (yes(s)/no):') #update
# print(att)


# #ex2:
# user={'ravi':'123','om':'345','virat':'1818'}
# username=''
# password=''
# while username not in user or password != user[username]:
#     username=input('username:')
#     password=input('password:')
# print(f'Hello {username}, welcome to dashboard')    



#-----Transfer statement
'''
1.pass : act as a placeholder in future.pass statement is a null operation that does absolutely 
2.continue : it is used to skip the current iteration . it is used in the loop
3.break : it is used to break the code
'''

# #wap to print odd number using the continue
# num=[1,2,3,4,5,6,7,8,9,10]
# for i in num:
#     if i%2==0:
#         continue
#     print(i)




#------import function from other file 


# for num in range(1,11):
#     continue
#     print(num)


 #import function from function.py

from Day23_function import factorial

factorial()




from Day23_function import square

square()     
