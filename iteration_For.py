#for loop :
    #      syntax:
             # for variable in iteration:
              #body



# number=[1,2,3,4,5]
# print('ravii')
# for num in number: #here num is a variable name 
#     print(num)
#     print('hello world')
# print('\nthe end')


# #accessing str character using for
# name='ravi'
# for name1 in name:
#     print(name1)

#wap to iterate all the numbers from a list
# number=[1,2,3,4,5,6]
# for num in number:
#     print(num)


#wap to print square of a numbers
# number=[1,2,3,4,5,6]
# print('before square')
# for num in number:
#     print(num**2) 


#wap to print list of cube of all numbers
# number=[1,2,3,4,5,6]
# cube=[]
# for num in number:
#     cb=num**3
#     cube.append(cb)
# print(cube)

#wap to print set of square of all numbers
# number=[1,2,3,4,5,6]
# sqaure=set()
# for num in number:
#     sq=num**2
#     sqaure.add(sq)
# print(sqaure)    


# #wap to cal sum of all numbers
# number=[1,2,3,4,5,6]
# sum=0
# for num in number:
#     sum=sum+num
# print(sum)

# #wap to substract all numbers from provided value
# number=[1,2,3,4,5,6]
# sub=25
# for num in number:
#     sub=sub-num
# print(sub)
   

#add total salary 
# employee=[('raj',20000),('pranav',40000),('ravi',50000)]
# total_sal=0
# for emp in employee:
#     salary=emp[1]
#     total_sal=total_sal+salary
# print(total_sal)    

#=======hw=====

# employee=[('raj',20000),('pranav',40000),('ravi',50000)]
# list=[]
# for emp in employee:
#     set=emp[1]
#     list.append(set)
#     sum=list[0]+[1]+[2]
# print(sum) 


#calculate avg salary 
employee=[('raj',20000),('pranav',40000),('ravi',50000)]
avg_sal=0
for emp in employee:
    avg=emp[1]
    avg_sal=avg/avg_sal
print(avg_sal)    

