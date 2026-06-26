# python-program

----emp details

name=input('enter your name:')
city=input("enter your city name:")
age=input('enter your age:')
gender=input("enter your gender:")
salary=int(input('enter salary :'))
dep=input('enter department name:')
print(f'\nyour name is : {name} \n salary is:{salary} \n department name is:{dep} \nyou are live in :{city} \nyou are {age} year old \nyour {gender}')



----arithematic operation

num1=int(input('enter num1='))
num2=int(input('enter num2='))
add=num1+num2
sub=num1-num2
mult=num1*num2
print(f'Addition of {num1} & {num2} is {add} \n substraction of {num1} C {num2} are {sub} \n multiplication of {num1} & {num2} is {mult}')


----sqare 
          sqr=num**2 
          sqr=num*num

num=int(input('enter number:'))
sqr=num**2
print(f'Square of a {num} is {sqr}')




----average

sub1=int(input('enter marks of sub1='))
sub2=int(input('enter marks of sub2='))
sub3=int(input('enter marks of sub3='))
sub4=int(input('enter marks of sub4='))
avg=(sub1+sub2+sub3+sub4)/4
print(f'Average is {avg}')


----increment %

salary=int(input('enter salary:'))
increment_percentage=int(input('enter increment % :'))
inc_salary=(salary*increment_percentage/100)
total_salary=inc_salary+salary
print(f'\nold salarty is:{salary} \n increment salary amount by:{inc_salary}  \n Total salary is :{total_salary}')


----discount

price=int(input('enter price:'))
discount=int(input('discount:'))
disc_price=(price*discount/100)
final_price=price-disc_price
print(f'price before discount is:"{price}\n discount price is:{disc_price}\n price after discount:{final_price}')
