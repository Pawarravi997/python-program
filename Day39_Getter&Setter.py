class Student:
    def __init__(self,nm,ag,mk):
        self.__Name=nm
        self.__Age=ag
        self.__Marks=mk

    def details(self):
        print(f'''
        Name  = {self.__Name}
        Age   = {self.__Age}
        Marks = {self.__Marks}
''')

    def get_name(self):
        username=input('enter username :')
        password=input('enter password :')
        if username=='ravi'and password=='1234':
            return self.__Name


    def set_name(self,nm):
        if isinstance (nm,str) and nm.isalpha():
            self.__Name=nm    

    def get_age(self):
         return self.__age           

s1=Student('ravi',22,90)   
# s1.details()      
# nm=s1.get_name() 
# print(nm)
s1.set_name('rahul')
s1.details()