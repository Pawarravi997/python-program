#-------Inheritance:
'''
>Inheritance is an object-oriented programming feature where a new class (child or subclass) takes on the attributes and methods of an existing class (parent or superclass).
>It is used in Python to reuse code, reduce duplication, and build organized, hierarchical relationships between different types of objects.
>inheritabnce is one the fundamental concept in object oriented programming .
>it allow a class (called a child/sub class) to inherit properties and method from another class (called a parent/super class)
>inheritance allow for code reuse and established a relatiopnship between the parent and child class. 
>the child class can use the functionalities of the parent class and also add its own unique behaviour

KEY FEACTURE:
1.code reusability--> the chlid class inheriut method and propertues from the parent cvlsdd treducing the need to reweite commn functionality
2.extensibility-->
3.method overrridding-->
4.hierchical reltionship-->


'''
# class parent:  #parent class which is contain the m1 and m2 method
#     def m1(self):
#         print('m1 method')
#     def m2(self):
#         print('m2 method')    

# class child(parent): #chlid class inherite the method of parent class and its own method also.
#     def m3(self):
#         print('m3 method')
#     def m4(self):
#         print('m4 method')          

# p=parent()  
# p.m1()     
# p.m2()  
# c=child()
# c.m4()


# class Account:
#     Bank_name='Maharashtra State Bank'
#     Ifsc='MAH67859'
#     Branch='Karve Nagar'

#     def __init__(self,nm,ac,bal):
#         self.Account_no=ac
#         self.Name=nm
#         self.balance=bal

#     def show_details(self):
#         print(f'''
#         Bank Name    = {Account.Bank_name}
#         Ifsc code    = {Account.Ifsc}
#         Branch Name  = {Account.Branch}
#         Name         = {self.Name}
#         Account n0.  = {self.Account_no}
#         Balance      = {self.balance}
#         ''')    

#     def check_balance(self):
#         print(f'Available Balance is : {self.balance}')

#     def Deposite_amount(self,amount):
#         if isinstance(amount,(int,float)):
#             if amount>0:
#                 self.balance=self.balance+amount
#                 return 'done'
#             else:
#                 return 'please enter the positive value only'  
#         else:
#             return "enter numeric value "      

#     def withdraw_amount(self,amount):
#         if isinstance(amount,(int,float)):
#             if amount>0:
#                 if amount<=self.balance:
#                     self.balance-=amount 
#                     return 'Done'
#                 else:
#                     return "insufficient balance"
#             else:
#                 return 'enter positive value'    
#         else:
#             return 'enter numeric value'    

# c=Account('ravi',789101,8000)
# c.show_details()    
# c.check_balance()  
# print(c.withdraw_amount(700))  
# c.check_balance()     
# c.Deposite_amount(50000)
# c.check_balance()
         
              
#--------Types of inheritance
'''
1.single inherritance
2.multiple inheritance
3.multilevel inheritance
4.hirrachical inheritance

'''
#---------------Single  inheritance

# class A:
#     def m1(self):
#         print('m1 method')

# class B(A):
#     def m2(self):
#         print('m2 method')

# parent=A()
# child=B()
# child.m1()
# child.m2()        

#-----------Mulple inheritance
# class A:
#     def m1(self):
#         print('m1 method')
# class B:
#     def m2(self):
#         print('m2 method')
# class C:
#     def m3(self):
#         print('m3 method')
# class D(A,B,C):
#     def m4(self):
#         print('m4 method')
# parent1=A()
# child=D()
# child.m1()   
# child.m3() 
# child.m2()                  


#---------------multilevel inheritance
# class A:
#     def m1(self):
#         print('m1 method')
#     def m2(self):
#         print('m2 method')    
# class B(A):
#     def m3(self):
#         print('m3 method')
#     def m4(self):
#         print('m4 method')    

# class C(B):
#     def m5(self):
#         print('m5 method')
#     def m6(self):
#         print('m6 method')   

# class D(C):
#     def m7(self):
#         print('m7 method')
#     def m8(self):
#         print('m8 method')

# parent=A()         
# parent.m2()
# child=D()
# child.m4()
# child.m1()



#---------------Hierachical inheritance

# class A:
#     def m1(self):
#         print('m1 method')
#     def m2(self):
#         print('m2 method')    
# class B(A):
#     def m3(self):
#         print('m3 method')
#     def m4(self):
#         print('m4 method')    

# class C(A):
#     def m5(self):
#         print('m5 method')
#     def m6(self):
#         print('m6 method')   
# parent=A()         
# child1=B()
# child2=C()
# child1.m1()
# child2.m1()


                    
#------MRO
'''
>method resolution order is the deterministic sequence pyhton uses to search for method or attributes in a class hierachy. 8
it is commuuted automativally ar class

'''

# #---practice LIBRARY MANAGEMENT SYSTEM
# '''
# '''
# class Library:
#     def __init__(self,ln):
#         self.Library_name=ln
#         self.Book_name={}
#         self.Count={}
#         # self.members=mem

#     def add_books(self,book_name,count):
#             self.Book_name[book_name]=self.Book_name[book_name]+count



#     def remove_books(self,book_name,bcount):
#             self.Book_name-=book_name
#             self.Count-=bcount  

#     def Display_books(self):
#             print(f'''
#             available books : {self.book_name}
#             count           : {self.bcount}
#         ''')
            
#     def issue_books(self,book_name,mem):
#             self.Book_name=book_name
#             self.member_name=mem


#     def return_books(self,book_name,mem):
#             self.Book_name=book_name
#             self.member_name=mem

# parent=Library('Dharmendra library','rich dad',20,'ravii')
# child=Display_book()
# child.Display_books()




class Book:
    def __init__(self, book_name, author, quantity):
        self.book_name = book_name
        self.author = author
        self.quantity = quantity

    def add_copies(self, count):
        self.quantity += count

    def remove_copy(self):
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False

    def display_book(self):
        print(f"Book Name : {self.book_name}")
        print(f"Author    : {self.author}")
        print(f"Quantity  : {self.quantity}")
        print("-" * 30)


class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name
        self.issued_books = []

    def issue_book(self, book):
        self.issued_books.append(book)

    def return_book(self, book):
        if book in self.issued_books:
            self.issued_books.remove(book)
            return True
        return False

    def display_member(self):
        print(f"Member ID   : {self.member_id}")
        print(f"Member Name : {self.member_name}")

        if len(self.issued_books) == 0:
            print("Issued Books: No books")
        else:
            print("Issued Books:")
            for book in self.issued_books:
                print(f"- {book.book_name}")

        print("-" * 30)


class Library:
    def __init__(self, library_name):
        self.library_name = library_name

        # Composition
        self.books = []
        self.members = []

    def add_book(self, book):
        for existing_book in self.books:

            if existing_book.book_name == book.book_name:
                existing_book.add_copies(book.quantity)
                print(f"{book.quantity} copies added to {book.book_name}")
                return

        self.books.append(book)
        print(f"Book '{book.book_name}' added to library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.member_name}' added successfully.")

    def remove_book(self, book_name, count):

        for book in self.books:

            if book.book_name == book_name:

                if book.quantity >= count:

                    book.quantity -= count

                    if book.quantity == 0:
                        self.books.remove(book)

                    print(f"{count} copies removed from '{book_name}'.")

                else:
                    print("Not enough copies available.")

                return

        print("Book not found.")

    def display_books(self):

        print("\n========== LIBRARY BOOKS ==========")
        print("Library:", self.library_name)

        if len(self.books) == 0:
            print("No books available.")
            return

        for book in self.books:
            book.display_book()

    def display_members(self):

        print("\n========== LIBRARY MEMBERS ==========")

        if len(self.members) == 0:
            print("No members registered.")
            return

        for member in self.members:
            member.display_member()

    def issue_book(self, book_name, member_id):

        book_found = None
        member_found = None

        # Find Book
        for book in self.books:
            if book.book_name == book_name:
                book_found = book
                break

        # Find Member
        for member in self.members:
            if member.member_id == member_id:
                member_found = member
                break

        # Check book
        if book_found is None:
            print("Book not found.")
            return

        # Check member
        if member_found is None:
            print("Member not found.")
            return

        # Check quantity
        if book_found.quantity <= 0:
            print("Book is not available.")
            return

        # Issue book
        book_found.remove_copy()
        member_found.issue_book(book_found)

        print(
            f"'{book_name}' issued to "
            f"{member_found.member_name}"
        )

    def return_book(self, book_name, member_id):

        member_found = None

        # Find Member
        for member in self.members:
            if member.member_id == member_id:
                member_found = member
                break

        if member_found is None:
            print("Member not found.")
            return

        # Find issued book
        book_found = None

        for book in member_found.issued_books:
            if book.book_name == book_name:
                book_found = book
                break

        if book_found is None:
            print(
                f"'{book_name}' is not issued "
                f"to {member_found.member_name}"
            )
            return

        # Remove from member
        member_found.return_book(book_found)

        # Check if book already exists in library
        library_book = None

        for book in self.books:
            if book.book_name == book_name:
                library_book = book
                break

        if library_book is not None:
            library_book.add_copies(1)
        else:
            self.books.append(
                Book(
                    book_found.book_name,
                    book_found.author,
                    1
                )
            )

        print(
            f"'{book_name}' returned by "
            f"{member_found.member_name}"
        )

# ==================================================
# MAIN PROGRAM
# ==================================================

# Creating Book objects
book1 = Book("Python Programming", "Mark Lutz", 5)
book2 = Book("Machine Learning", "Andrew Ng", 3)
book3 = Book("Data Science", "John Smith", 4)


# Creating Member objects
member1 = Member(101, "Vaibhav")
member2 = Member(102, "Rahul")
member3 = Member(103, "Amit")


# Creating Library object
library = Library("ABC Central Library")


# Adding books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


# Adding members
library.add_member(member1)
library.add_member(member2)
library.add_member(member3)


# Display books
library.display_books()


# Display members
library.display_members()


# Issue books
print("\n========== ISSUE BOOK ==========")

library.issue_book("Python Programming", 101)
library.issue_book("Machine Learning", 102)
library.issue_book("Data Science", 103)


# Display books after issuing
library.display_books()


# Display members after issuing
library.display_members()


# Return book
print("\n========== RETURN BOOK ==========")

library.return_book("Python Programming", 101)


# Display books after return
library.display_books()


# Display members after return
library.display_members()


# Remove books
print("\n========== REMOVE BOOK ==========")

library.remove_book("Machine Learning", 1)

library.display_books()





















