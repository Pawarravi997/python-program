# #--------Class Method:
# '''
# >it is used to perform an operation 
# >
# >
# >


# '''



# class Student:
#     course='python'
#     trainer='Vaibhav'
#     fees=50000
#     def __init__(self,rll,nm,ag):
#         self.roll=rll
#         self.name=nm
#         self.age=ag
#         self.marks={}
#     def show_details(self):
#         details=f'''
#                 roll number={self.roll}
#                 Name={self.name}
#                 age={self.age}
#                 course={self.course}
#                 Trainer={self.trainer}

#                 '''
#         print(details)

#     def add_marks(self,testname,mk):
#         self.marks[testname]=mk  
#         return 'Done'  

#     def cal_percentage(self):
#         obt=0
#         for mk in self.marks.values():
#             obt=obt+mk
#         total=100*len(self.marks)
#         per=obt/total*100
#         return per
#     def show_result(self):
#         per=self.cal_percentage()
#         if per>40:
#             return "Pass"
#         else:
#             return "Fail"
#     @classmethod  
#     def apply_discount(cls,dis):
#         dp=cls.fees*dis/100
#         sp=cls.fees-dp
#         return sp

#     @classmethod
#     def change_trainer(cls,trainer):
#         cls.trainer=trainer
#         return "Done"

    
# s1=Student(1,'ravi',22)    
# s2=Student(2,'om',25) 
# print(s1.apply_discount(15)) 
# print(s1.change_trainer('nikhil'))


# #------------Static Method:
# '''
# >Static method is method that belongs tpo a class but does not use instance(self) or(cls)  and it is defined using static method decorator 
# >does not take self or parameter can we call either class name or subject
# >it is used for utility or helper functions related to the class
# '''

# @staticmethod
# def passing_method():
#     print('passing marks 40')

# @staticmethod
# def percentage(obt,total):
#     per=obt/total*100
#     return per    
# s1=percentage(340,500)
# print(percentage())




#----------Task:
'''
Employee Payroll System:
create a classs employee with atteributes: empid,name,basic salary.
requirement:
>constructoie should initilize tha atribute
>method calclulate allowances()>HRA=20% DA=10%
>method calculate gross salary()>basic+hra+da
>method calculate net salary()>gross-tax(10% of gross)
>method display oayslip()>shoe emp details and  full salary calculation
'''

class Employee:
    company="Google"
    HRA=20
    DA=10

    def details(self,id,nm,sal):
        self.empid=id
        self.name=nm
        self.salary=sal

    def cal_Allowance(self):
        HRA_Amount=self.salary*Employee.HRA/100
        DA_amount=self.salary*Employee.DA/100
        return HRA_Amount,DA_amount
   
    def Gross_sal(self):

        G_sal=self.salary+self.
        return Final_sal

    def  Gross_tax(self):
        tax=self.Gross_sal*10/100
        return tax

    def Empd_details(self):
        total_sal=self.cal_Allowance()
        sal_slip=(f'''
                Employee id={self.empid}
                Employee Name={self.name}
                Employee salary={self.salary}
                Employee total salary={self.}

            ''')

e1=Employee()           