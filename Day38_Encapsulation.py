#-------Encapsulation:
'''
>Encapsulation in Python is the object-oriented programming (OOP) practice of bundling data (attributes) and methods (functions) into a single unit (a class) while restricting direct access to some of the object's components.

'''

#we can acces or modify the public attribute 
# class Machine:
#     Brand_name='TATA'
#     def __init__(self,mname):
#         self.Machine_name=mname
#         self.in_count=0 #private atrribut
#         self.out_count=0

#     def display_count(self):
#         print(f''''
#             Welcome to {self.Machine_name}
#             In count  = {self.in_count}
#             Out count = {self.out_count}
#               ''')    

#     def increase_inCount(self):
#         self.in_count+=1

#     def increase_outCount(self):
#         self.out_count+=1

#     def reset(self):
#         self.in_count=0
#         self.out_count=0

# dmart=Machine('dmart')
# dmart.display_count()
# dmart.increase_inCount()
# dmart.increase_inCount()
# dmart.increase_inCount()
# dmart.increase_inCount()
# dmart.increase_inCount()
# dmart.display_count()
# dmart.increase_outCount()
# dmart.increase_outCount()
# dmart.increase_outCount()
# dmart.increase_outCount()
# dmart.display_count()




#we cannot acces and modify the private atrribute 
#__ (double underscore used before for making the atrribute as private)
#also method can make private using the double underscore before the method name
class Machine:
    Brand_name='TATA'
    def __init__(self,mname):
        self.Machine_name=mname
        self.__in_count=0    #private atribute
        self.__out_count=0  #private atribute

    def display_count(self):
        print(f''''
            Welcome to {self.Machine_name}
            In count  = {self.__in_count}
            Out count = {self.__out_count}
              ''')    

    def increase_inCount(self):
        self.__in_count+=1

    def increase_outCount(self):
        self.__out_count+=1

    def reset(self):
        self.__in_count=0
        self.__out_count=0

dmart=Machine('dmart')
dmart.display_count()
dmart.increase_inCount()
dmart.increase_inCount()
dmart.increase_inCount()
dmart.display_count()
dmart.increase_outCount()
dmart.increase_outCount()
dmart.display_count()
