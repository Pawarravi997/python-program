#if elif else used when multiple condition applied.

#ex1:
# print("start")
# num=int(input('enter a number:'))
# if num>0:
#     print(f'{num} is a positive number')
# elif num<0:
#     print(f'{num} is a negative number')
# else:
#     print(f'{num} is a zero')
# print('the end')          

#ex2:
# print('welcome')
# age=int(input('enter age:'))
# if age<18:
#     print('you are a child')
# elif age>=18 and age<60:
#     print('you are adult')
# elif age>60:
#     print('you are ss') 
# else:
#     print('you are old')    



#ex3:
#divisibility checks

# num=int(input('enter a number:'))
# if num%3==0 and num%5==0:
#     print(f'{num} divisible by 3')
# elif num%5==0:
#     print(f'{num} divisible by 3')
# elif num%3==0 :
#     print(f'{num} divisible by 3 and 5') 
# else:
#     print('not divisible by 3 and 5')  
#   


#ex4:
#grade calculator

# marks=int(input('enter marks:'))
# if marks>=90:
#     print("A grade")
# elif marks<=89 and marks>=75:
#     print('B grade')
# elif marks<=74 and marks>=60:
#     print("C grade")
# elif marks<=59 and marks>=40:
#     print('D grade') 
# else:
#     print('Fail')       


#ex5:
#electricity bill

# amount=int(input('enter bill amount:'))
# if amount>=2000:
#     disc=amount-(amount*15/100)
#     print(f'amount after discount is {disc}')
# elif amount>1500 :
#     disc=amount-(amount*10/100)
#     print(f'amount after discount is {disc}')
# elif amount>1000 :
#     disc=amount-(amount*5/100)
#     print(f'amount after discount is {disc}')
# elif amount<1000:
#     print(f'no discount,final bill amount is {amount} ')


#ex6:

product_mrp={'p1':70000,'p2':40000,'p3':20000,'p4':10000,'p5':30000,'p6':90000,'p7':44000}
product_price={}
for name,price in product_mrp.items():
    if price>=65000:
        sp=price-(price*20/100)
    elif price>36000:
        sp=price-(price*15/100)
    elif price>11000:
        sp=price-(price*10/100)
    else:
        sp=price-(price*5/100)

    # print(f'product selling price after disc is {sp}')        
    product_price[name]=sp
print(product_price)