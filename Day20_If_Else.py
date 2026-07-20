student_marks={'ompatil':79,"umesh wagh":20,'prathmesh gandhi':79,'pratik tayde':67,'rahul boyar':31,'suraj chavan':90,'vijay chopade':23}

#ex1:

#wap to print name of student in a list without using keys
s_name=[]
# for name in student_marks:
#     s_name.append(name)
# print(s_name) 

#ex2:
#wap to print all marks of student in list
s_marks=[]
# for marks in student_marks.values():
#     s_marks.append(marks)
# print(s_marks)

#ex3:
#wap to print name of pass student which can score grater than 40.
pass_student=[]
# for name,marks in student_marks.items():
#     if marks > 40:
#         pass_student.append(name)
# print(pass_student)    

#ex4:    
#wap tp print list of a fail student name and pass student  name 
# pass_student=set()
# fail_student=[]
# for name,marks in student_marks.items():
#     if marks >40:
#         pass_student.add(name)
#         total_pass_student=len(pass_student)
#     else:
#         fail_student.append(name)
#         total_fail_student=len(fail_student)
# print(f'total pass student is:{total_pass_student} those name are:{pass_student}')
# print(f'total fail student is:{total_fail_student} those name are:{fail_student}')         

#ex5:
# student_marks={'ompatil':79,"umesh wagh":20,'prathmesh gandhi':79,'pratik tayde':67,'rahul boyar':31,'suraj chavan':90,'vijay chopade':23}
# #wap to print dict of final result-->{'ompatil':'pass','umesh wagh':'fail'}
# d1={}
# for name,marks in student_marks.items():
#     if marks>40:
#         d1[name]='pass'
#     else:
#         d1[name]='fail'
# print(d1)        


emp_salary={'ompatil':79000,"umesh wagh":20000,'prathmesh gandhi':79000,'pratik tayde':67000,'rahul boyar':31000,'suraj chavan':90000,'vijay chopade':23000}

#ex6:
#wap to print total emp salary count less than 50k
# count=0
# for salary in emp_salary.values():
#     if salary<50000:
#         count += 1

# print(count)            
        
# #ex7:
# #wap to print total emp salary count less than 50k and more than 50k
# less_count=0
# greater_count=0

# count=0
# for salary in emp_salary.values():
#     if salary<50000:
#         less_count += 1
#     else:
#          greater_count +=1 

# print(f'salalry count above 50k is:{greater_count} salalry count less 50k is:{less_count}')      

#ex8:
emp_salary={'ompatil':79000,"umesh wagh":20000,'prathmesh gandhi':79000,'pratik tayde':67000,'rahul boyar':31000,'suraj chavan':90000,'vijay chopade':23000}

#wap to print salary after 10% increment in the new dict
# final_salary={}
# for name,salary in emp_salary.items():
#     total_sal=(salary*10/100)+salary
#     final_salary[name]=total_sal
# print(final_salary)    

#ex9:
#wap to print extra salary after increment only those salary returns
# final_salary={}
# total=0
# for name,salary in emp_salary.items():
#     inc=salary*10/100
#     total_sal=salary+inc
#     final_salary[name]=total_sal
#     total=total+inc
# print(sum)    


emp_salary={'ompatil':79000,"umesh wagh":20000,'prathmesh gandhi':79000,'pratik tayde':67000,'rahul boyar':31000,'suraj chavan':90000,'vijay chopade':23000}

#ex10:
#wap to print salary above 50k add 10% increment   and less 50k add 5%increment 
# final_salary={}   
# for name,salary in emp_salary.items():
#     if salary >50000:
#          sal=salary*10/100
#          new_sal=salary+sal
#          final_salary[name]=new_sal
#     else:
#          sal=salary+5/100
#          new_sal=salary+sal
#          final_salary[name]=new_sal
# print(final_salary)  
#        
#----------or

# final_salary={}   
# for name,salary in emp_salary.items():
#     if salary >50000:    
#          final_salary[name]=salary*0.1+salary
#     else:
#          final_salary[name]=salary*0.05+salary   
# print(final_salary)         
