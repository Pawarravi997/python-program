'''
syntax for if else in lambda:
                                lambda parameter : expression1 IF condition ELSE expression2
'''


#ex1:
# check=lambda num: 'Even' if num%2==0 else "Odd"
# print(check(7))


#ex2:
#create a function to check a number divisible by 10 or not
# check=lambda num : 'true' if num%10==0 else 'false'
# print(check(370))
# print(check(50))
# print(check(700.00))
# print(check(680.90))


#ex3:
#wap to apply discount if amount is greater than 10k aplly 10% discount and less than 10k apply 5%
# final=lambda amount: amount-amount*10/100 if amount>10000  else amount-amount*5/100
# print(final(120000))
# print(final(8000))


#ex4:
#wap to check a student pass or fail
# result=lambda marks: 'pass' if marks>35 else 'fail'
# print(result(70))


#ex5:
#wap to create a function which is give grade according ti their marks 
#>90 A
#>=70 B
#>=50 c
#< fail
# grade=lambda marks: 'A' if marks>90 else 'B' if marks>=70 else 'C' if marks>=50 else 'fail' 
# print(grade(65))



#-----------------filter practice----------------------

#ex1:
# student=['ravi','om','shiv','rajaram','nitin']
# print(list(filter(lambda name: len(name)<5,student)))


#ex2:
# #print list of name passed student
# result={'ravi':90,'om':40,'shiv':70,'rajaram':33,'nitin':65}
# print(list(filter(lambda name: result[name]>50,result)))

#ex3:
#wap to print dict of fail student name
# result={'ravi':90,'om':40,'shiv':20,'rajaram':33,'nitin':65}
# print(dict(filter(lambda name: name[1]<40 ,result.items())))
# print(dict(filter(lambda t : t[1]<60,result.items())))




#-----------------Map 
'''
>The map() function in Python is a built-in tool used to apply a specific function to every item in an iterable (such as a list, tuple, or dictionary) without using an explicit for loop
>map() function in Python applies a function to every element of one or more iterables and returns a map object (iterator) containing the transformed results
syntax:
       map(function,iteratble)
'''
# #ex1:
#wap to add 5 in each numner
# numbers=[10,20,30,40,50,60,70,80,90,100]
# print(list(map(lambda num: num+5,numbers)))


#ex2:
#wap to print square of all numbers
# numbers=[10,20,30,40,50,60,70,80,90,100]
# print(list(map(lambda sqr: sqr**2,numbers)))


#ex3:
#wap to capital first letter of each words
# student=['kunal thakur','ravi pawar','om kendre','rohit sharma','virat kohli']
# print(list(map(lambda name: name.title(),student)))


#ex4:
#wap to reverse all list 
# student=['kunal thakur','ravi pawar','om kendre','rohit sharma','virat kohli']
# print(list(map(lambda name: name[: :-1],student)))

#ex5:
#print dict of a square of each number
# number=[1,2,3,4,5,6,7,8,9,10]
# print(dict(map(lambda sqr: (sqr ,sqr**2),number)))


#ex6:
#print dict to represent total numebr of character
# student=['kunal thakur','ravi pawar','om kendre','rohit sharma','virat kohli']
# print(dict(map(lambda name:(name,len(name.replace(" ",""))),student)))

#ex7:
# student=['kunal thakur','ravi pawar','om kendre','rohit sharma','virat kohli']
# print(list(map(lambda name:name.capitalize(),student)))
# print(list(map(lambda name:name.title(),student)))
# print(list(map(lambda name:name.upper(),student)))
# print(list(map(lambda name:name.lower(),student)))



#ex8:
#wap to print dict of price after discount

# products_mrp={'p1':20000,'p2':60000,'p3':40000,'p4':10000}
# map(lambda price: price[1]products_mrp)


















#----------------Reduce
'''
>The reduce() function in Python applies a function cumulatively to the elements of an iterable to return a single final value. It is part of the standard library's functools module, meaning you must import it before use.

'''

# from functools import reduce
# numbers = [1, 2, 3, 4]
# result = reduce(lambda num, curr: num + curr, numbers)

# print(result)  # Output: 10



for details in shopping_customers.values():
    if sum(details["orders"])>15000:
        print(details["name"])
