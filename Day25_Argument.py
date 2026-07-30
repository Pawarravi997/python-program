#---positional argument
'''
these argumnet are passed to the function based on their posotion in the function call. the order in which the argumnet are passed must match the order of the parameter in the function defination. and number of argumnet is equal to the number of parameter.
'''

# def full_name(fn,mn,ln):
#     fname=f' {fn} {mn} {ln}'
#     print(fname)
# full_name('rohan','shubash','kambale')


#---keyword argument
'''
these argumnet are passed to the function by explicitly specifying the name of the parameter along with the value.the order of the argument dose not matter.
'''

# def full_name(fn,mn,ln):
#     fname=f' {fn} {mn} {ln}'
#     print(fname)
# full_name(mn='rohan',ln='shubash',fn='kambale')



#---Default argument
'''
these are parameter that have a default value.if no argumnrt is provided for that parameter, the default value is used.
'''
# def course_detail(cname,duration,institute='the kiran academy'):
#     data = f'''
#         institute name={institute}
#         course name={cname}
#         duration={duration}
# '''
    # print(data)
# course_detail('java','4 month','the kiran academy')    
# course_detail('python','4 month','the kiran academy')    
# course_detail('aws','4 month')   
# course_detail('Ai/Ml','4 month','java by kiran')     
    

#===================postional and keyword argument how to use both type of argumnet and parameter pass=====
# def course_detail(cname,duration,institute='the kiran academy'):
#     data = f'''
#         institute name={institute}
#         course name={cname}
#         duration={duration}
# '''
#     print(data)
# course_detail()  



#arbitary argument
#1.positional arbitary argument::this allow you to pass a varible number of positional argumnet to the function. the *args syntax collects extra argument as a tuple

# def fname(*args):
#     print(args)
# fname('ravi','om','shubham','radha','kishor')
# fname('ravi','om','shubham')        

#2.keyword arbitary argument::



# def percentage(**kwargs):
#     obt=0
#     for mk in kwargs.values():
#         obt=obt+mk
#     total=len(kwargs)*100
#     per=obt/total*100
#     print(per)
# percentage(t1=40,t2=50,t3=90,t4=33)  
  


#-----multiple postional arbitary argument and multiple keyword arbitary argumment
# def sum_of_number(*args,**kwargs):
#     if args:
#         print(args)
#     else:
#         print(kwargs)
# sum_of_number(10,20,30,40)
# sum_of_number(n1=10,n2=20,n3=30,n4=40)



#return: the return statemnt in python is usedd inside a function to send a value or result 
#never excute code which is written after the return statment
#return statment is used only once in the block
#multiple return statement used by comma seprated

# def percentage(obt,total):
#     per=obt/total*100
#     print(per)
# percentage(50,100)   
 
# def percentage(obt,total):
#     per=obt/total*100
#     return per
#     print('thank you')
# print(percentage(50,100)) 
# result=percentage(340,500)
# print(result)

# def percentage(obt,total):
#     per=obt/total*100
#     print('thank you')
#     return per
# print(percentage(50,100)) 
# print(percentage(340,500)) 


def cal(n1,n2):
    sum=n1+n2
    sub=n1-n2
    return sum, sub
print(cal(100,40))
result=cal(100,40)
print(result)
sum,sub=cal(100,40)
print(sum)
print(sub)