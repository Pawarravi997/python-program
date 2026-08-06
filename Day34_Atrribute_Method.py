#--------Attribute
'''
>A variable that belongs to a class or an object — it stores data/state. Accessed using dot notation (object.attribute).

Types of Attributes
1. Instance Attributes

>this attribute is create as object level
>Belong to a specific object, defined usually inside __init__ using self.
> Each object gets its own copy — changing one doesn't affect others.
class Student:
    def __init__(self, name, marks):
        self.name = name      # instance attribute
        self.marks = marks    # instance attribute

s1 = Student("Ravi", 84)
s2 = Student("Amit", 90)
s1.name  # "Ravi" — separate from s2

2. Class Attributes

>Belong to the class itself, shared by all objects. 
>Defined directly inside the class body (outside any method). 
>Changing it via the class affects all instances that haven't overridden it.
>you can access the class attribute using the object reference as well as class name. you can acces using class its good practice
class Student:
    college = "SRTM"   # class attribute — shared

    def __init__(self, name):
        self.name = name

s1 = Student("Ravi")
s2 = Student("Amit")
print(Student.college) #access using clas
print(s1.college, s2.college)  # SRTM SRTM (same for both)

⚠️ Common trap: if you do s1.college = "IIT", it doesn't change the class attribute — it creates a new instance attribute on s1 that shadows the class one. s2.college still stays "SRTM".

3. Private Attributes (Name Mangling)

Prefixed with double underscore __ — Python "mangles" the name internally (_ClassName__attr) to discourage direct outside access. This is Python's version of encapsulation (not true privacy).

python
class Student:
    def __init__(self, marks):
        self.__marks = marks   # private-ish

    def get_marks(self):
        return self.__marks

'''
# class xyz:
#     A='aaa'  #class attributes(inside class and outside the constucor or def)
#     B='bbb'  #class attributes
#     def __init__(self,v1,v2):
#         self.value1=v1 #instance attributes(inside the constructor)
#         self.value2=v2 #instance attributes
#     def method1(self) :
#         result=self.value1*10  #local attributes
        #   return result



#----------instance Attribute (object level )

# class Student:
#     def __init__(self,nm,ag):
#         self.name=nm
#         self.age=ag
# s1=Student('ravii',22)
# s2=Student('om',20)
# print(s1.name)
# print(s1.age)
# print(s2.name)
# print(s2.age)


# #create a employee class with at least 4 instance attributes
# class Employee:
#     def __init__(self,nm,id,sal,depart):
#         self.name=nm
#         self.empid=id
#         self.salary=sal
#         self.department=depart
# e1=Employee('ravi',101,70000,'manager') 
# e2=Employee('om',102,60000,'Hr') 
# print(e1.name)
# print(e2.salary)


# #create a Books class with at least 3 instance attributes
# class Books:
#     def __init__(self,nm,aut,publi):
#         self.name=nm  #instance attribute
#         self.author=aut
#         self.published=publi
# b1=Books('the end is the beggining','ravi',2025)        
# b2=Books('Rich dad poor dad','om',2024) 
# print(b1.name)
# print(b2.published)



#----------Class/static Attribute (class level)

#1.
# class Student:
#     institute='TKA'
#     course='Python'
#     duration='6 month'
#     fees=50000
#     trainer='vaibhav'
#     def __init__(self,nm,ag,ci):
#         self.name=nm
#         self.age=ag  #instance attribute
#         self.city=ci
# s1=Student('ravi',22,'karve nagar')    
# s2=Student('virat',25,'swargate') 
# print(s1.name,s1.age,s2.name,s2.age)  
# print(Student.course,Student.fees) 


#2.
# class Employee:
#     company='Google' #class attribute
#     location='pune'
#     owner='Dharmendra pradhan'
#     def __init__(self,id,nm,sal,ag):
#         self.name=nm
#         self.empid=id  #instance attribute
#         self.age=ag
#         self.salary=sal
# e1=Employee('ravi',101,50000,22)
# e2=Employee('virat',102,70000,34)
# print(Employee.location)
# Employee.location='Hadapsar'#here we can update the value of the varible using that class .cause this reflect in all the programes
# print(e1.name,e2.salary)
# print(e1.company,e2.location) #access using object reference


#3.
# class mobileShop:
#     shopname='dharmendra mobile shop' 
#     location='pakistan'
#     def __init__(self,br,mod,pr,stor):
#         self.Brand=br #instance attribute
#         self.model=mod
#         self.price=pr
#         self.storage=stor
# m1=mobileShop('Samsung','A17',30000,'128 Gb') 
# m2=mobileShop('iphone','17 pro',130000,'1 TB') 
# m1=mobileShop('vivo','v30e',45000,'256 Gb') 
# print(m1.shopname)
# print(m1.Brand)
# print(m2.price)
# print(mobileShop.location)
# mobileShop.shopname='rahul Gandhi mobile shop'
# print(mobileShop.shopname)



#----------Local Attribute  (method level)
'''
method is used to perform an operation on the data
types:
      1.instance method
      2.class method
      3.static method

'''
#hw
# student details(name,age,marks) shoe deyails,add marks,calculate percentage,show result then import from another module

# interview question
# what is attribute and types
# all types with ex
# what is methodd and types
# explain types with syntax and ex and also special method(dundor method)



class Student:
    course='python'
    trainer='Vaibhav'
    def __init__(self,rll,nm,ag):
        self.roll=rll
        self.name=nm
        self.age=ag
        self.marks={}
    def show_details(self):
        details=f'''
                roll number={self.rll}
                Name={self.name}
                age={self.age}
                course={self.course}
                Trainer={self.trainer}
'''
        print(details)

    def add_marks(self,testname,mk):
        self.marks[testname]=mk  
        return 'Done'  

    def cal_percentage(self):
        obt=0
        for mk in self.marks.values():
            obt=obt+mk
        total=100*len(self.marks)
        per=obt/total*100
        return per
    def show_result(self):
        per=self.cal_percentage
        if per>40:
            return "Pass"
        else:
            return "Fail"
s1=Student(1,'ravi',22)    
s2=Student(1,'om',25)  
print(s1.name)
print(s2.course)    
print(s1.show_details)              
            