#----Append method (append value/object at the end of the list)
#            variable_name=(object/value) 


# number=[10,20,30,40,50]
# number.append(60)  # when you apply append function they only append value and return none thats why we canot print () use
# number.append('ravi')
# print(number)


#----insert method (insert is used to add value/object before provide index number)
#           variable_name=(index_number,object/value) 

# number=[10,20,30,40,60,70]
# number.insert(0,0)
# print(number)
# number.insert(4,50)
# print(number)

# number=[10,20,30,40,60,70,80,90]
# number.insert(-4,50)
# print(number)

# name=['ravi','pawar']
# name.insert(1,'udhav')
# print(name)


#----index method (index is used to change or add the value using their index number )
#             var_name=[index]=value


# number=[10,20,30,44,50,60]
# number[3]=40
# print(number)
# name=['raja','nitin','ravi','virat',50,'raju']
# name[-2]='kiran'
# print(name)
# number=[10,20,30,44,55,60,70,80]
# number[3:5]=[40,50]
# print(number)
# number=[10,20,30,44,55,66,70,80,90]
# number[3:7]='ravi'
# number[3:7]=['ravi']
# number[3:7]=['ravi','rohan','virat']
# print(number)



#----delete method
#            remove= used to delete direct provided value from the list and return none
#            pop= if duplicate value is in list so we can used pop for delete value using the index andreturn the any value like int,float,str etc..
#            clear= used to clear all list element and return none

#===========================remove========================

# number=[10,20,30,40,50,66,70,80]
# number.remove(66)
# print(number)

#===========================pop========================

# number=[10,20,30,40,50,66,70,80,90,66]
# number.pop() #if i donot provide index it will delete -1 value by default value
# number.pop(5)
# print(number)

#===========================append and pop========================

# n1=[10,20,30,40,50,60,70]
# n2=[101,80,102,103,104,105]
# n2.pop(1)
# n1.append(n2.pop(1))  # it means firstly pop the index value then append into n1 at the end
# print(n2)
# print(n1)

#===========================clear========================

# number=[10,20,30,40,50,66,70,80,90,66]
# number.clear()
# print(number)


#===========================del function========================
#                  del var_name[index]

# number=[10,20,30,40,50,66,70,80,90]
# del number[5]
# print(number)

#=========================Acess====================================

# courses=['data science','data analytics','power Bi','aws']
# print(courses[-2]) #acess 1 value using index
# print(courses[:-2]) #acess using slicing
# courses[2]='python'
# print(courses) #add after data analytics
# courses.insert(3,'python') #add by using the insert using the index value
# print(courses)

#=========================update====================================

# courses=['data science','data analytics','power Bi','aws']
# courses[1]="DA" #replace data analytics by DA
# print(courses)
# courses[0:2]=["DS","DA"] #replace using slicing
# print(courses)

#=========================delete====================================

# courses=['data science','data analytics','power Bi','aws','power Bi']
# courses.remove('aws') #delete aws using remove
# print(courses)
# courses.pop() #it delet -1 index value by default using pop
# print(courses)

# courses=['data science','data analytics','power Bi','aws','power Bi']
# courses.clear()
# print(courses)
# del courses[1:-1:1]
# print(courses)

#=========================reverse====================================

# courses=['data science','data analytics','power Bi','aws','power Bi']
# courses.reverse()
# print(courses)

#=========================sort====================================

# num=[10,20,40,50,30,3]
# num.sort()
# print(num)

#=========================count====================================

# num=[10,20,40,50,30,3.50,80,10]
# print(num.count(10))

