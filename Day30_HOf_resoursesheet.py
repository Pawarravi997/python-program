'''
1)what is Higher Order Function ?
Answer:
A Higher-Order Function is a function that either takes another function as an argument, returns a function as its result, or both. It is used to create reusable and modular code by working with functions as first-class objects.

2)what are common built-in Higher Order Functions in Python??
Answer:
built-in Higher Order Functions are
1.filter
2.map
3.reduce

3)What is the filter() function in Python?
Answer:
The filter() function in Python is used to filter elements from an iterable (like a list, tuple, or set) based on a condition specified by a function. It takes two arguments:
A function that returns a Boolean value (True or False).
An iterable to be filtered.
The filter() function returns a filter object, which can be converted to a list, tuple, etc.
syntax:
	var=filter(fun,iterable)
eg.
numbers=[1,2,3,4]
even=list(filter(lambda num : num%2==0 ,numbers))
print(even)   #[2,4]

4)How does the filter() function work internally?
Answer:
The filter() function applies the given function to each element of the iterable. If the function returns True, the element is included in the result; otherwise, it is excluded. The process stops once all elements in the iterable are processed.

5)Can filter() be used without a function?
Answer:
Yes, the filter() function can be used without passing a function by using None as the first argument. In this case, it filters out all values that are falsy (e.g., 0, None, False, '').

eg.
data = [0, 1, '', None, 'Python', False]
filtered = filter(None, data)
print(list(filtered))  # Output: [1, 'Python']

6)What are the key differences between filter() and a list comprehension for filtering?
Answer:
filter():
-------
Functionality=>Uses a function to filter data.	
Performance=>May be faster for large datasets.	
Readability=>Readable for simple conditions.	
List Comprehension :
-----------------
Functionality=>Uses inline conditional expressions.
Performance=>May be slower for large datasets.
Readability=>Readable and flexible for complex logic.

7)Can the filter() function work with multiple arguments in the filtering function?
Answer:
No, the function passed to filter() must take only one argument. If you need to use multiple arguments, you can use a lambda function with additional arguments passed as global variables or through partial application.
eg.
numbers = [10, 15, 20, 25, 30]
num = 20
filtered = filter(lambda x: x > num, numbers)
print(list(filtered))  # Output: [25, 30]

8)What is the map() function in Python?
Answer:
The map() function in Python applies a given function to each item in an iterable (like a list, tuple, or set) and returns a map object (an iterator) containing the results. It takes two arguments function and iterable
The syntax is:
var=map(fun,iterable)

eg.
numbers=[10,20,30,40,50]
#increase each number by 5
new_list=list(map(lambda num : num+5 ,numbers))
print(new_list)    #[15,25,35,45,55]

9)Can the map() function work with multiple iterables?
Answer:
Yes, map() can work with multiple iterables, but the function must accept the same number of arguments as the number of iterables provided. The process stops when the shortest iterable is exhausted.
eg.
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1 , numbers2)
print(list(result))  # Output: [5, 7, 9]

10)What is the return type of map()?
Answer:
The map() function returns a map object, which is an iterator. To view the results, you must convert it into a list, tuple, or another iterable type.

eg.
nums = [1, 2, 3]
result = map(lambda x: x**2, nums)
print(result)          # Output: <map object at ...>
print(list(result))    # Output: [1, 4, 9]

11)Can the map() function handle None as the first argument?
Answer:
No, the map() function requires a valid function as its first argument. Unlike filter(), which can use None, map() does not perform any default operation when None is passed.

12)What is the reduce() function in Python?
Answer:
The reduce() function, part of the functools module, applies a given function cumulatively to the items in an iterable, reducing it to a single value. It works by taking two elements at a time, applying the function, and then using the result as the first argument for the next operation.

Example:
from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums)
print(result)  # Output: 10

explanation:
First iteration: x = 1, y = 2 â†’ x + y = 1+2 = 3
Second iteration: x = 3 (result), y = 3 â†’ x + y = 3+3= 6
Third iteration: x = 6(result), y = 4 â†’ x + y = 6 + 4 = 10

13)How does the reduce() function work internally?
Answer:
The reduce() function works as follows:
It takes the first two elements of the iterable and applies the given function.
The result is combined with the next element in the iterable.
This process continues until all elements are processed, resulting in a single value.

14)What are the main arguments required by reduce()?
Answer:
The reduce() function requires the following arguments:

Function: A callable that takes two arguments and performs an operation.
Iterable: The data (e.g., list, tuple) to be reduced.
Optional Initial Value: A starting value that is combined with the first element of the iterable.

eg.
from functools import reduce

nums = [1, 2, 3]
result = reduce(lambda x, y: x + y, nums, 10)  # Initial value is 10 means x=10
print(result)  # Output: 16

Explanation:
The initial value (10) is used as the starting value for x.
The function applies the following steps:
First iteration: x = 10, y = 1 â†’ x + y = 10 + 1 = 11
Second iteration: x = 11(result), y = 2 â†’ x + y = 11 + 2 = 13
Third iteration: x = 13(result), y = 3 â†’ x + y = 13 + 3 = 16
The final result is 16.

-------------------------
Logical
1.Given a list of strings, filter out the ones with more than 5 characters.
Solution:

words = ["apple", "banana", "cat", "elephant", "dog", "grape"]
long_words = filter(lambda x: len(x) > 5, words)
print(list(long_words))  # Output: ['banana', 'elephant']


2. Filter numbers divisible by 3
Write a program to filter numbers from a list that are divisible by 3.

Solution:
nums = [3, 5, 9, 12, 15, 17, 20]
divisible_by_3 = filter(lambda x: x % 3 == 0, nums)
print(list(divisible_by_3))  # Output: [3, 9, 12, 15]

3. Filter non-empty strings
From a list of strings, filter out all empty strings.
Solution:
strings = ["Python", "", "Code", " ", "Filter", ""]
non_empty = filter(lambda x: x.strip() != "", strings)
print(list(non_empty))  # Output: ['Python', 'Code', 'Filter']

4. Filter Passing Students names only
Solution:
students = {
    "Amol": 45,
    "Suraj": 78,
    "Ved": 88,
    "Siddhi": 55,
    "Payal": 33,
    "Ragini": 99,
    "Samruddi": 49
	}

passing_students = list(filter(lambda name: students[name] >= 50, students))
print(passing_students)  # Output: ['Suraj', 'Ved', 'Siddhi', 'Ragini']

5.Given a dictionary of students and their percentages, filter out only the students who have passed (percentage >= 50). Return the result as a dictionary.
solution:
# Dictionary of students with their percentages
students = {
    "Amol": 45,
    "Suraj": 35,
    "Ved": 88,
    "Siddhi": 55,
    "Payal": 33,
    "Ragini": 60,
    "Samruddi": 99
	}

passing_students = dict(filter(lambda x: x[1] >= 50, students.items()))

print(passing_students) 

#{'Ved': 88, 'Siddhi': 55, 'Ragini': 60,"Samruddi": 99}


6):
Given a list of numbers, double each element using the map() function.
Solution:
nums = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, nums)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]

7. Convert a List of Strings to Uppercase
Given a list of strings, convert each string to uppercase using map().
Solution:
names= ["dishant", "rajput", "sakshi", "shiddi"]
uppercase_names = map(lambda name: name.upper(), names)
print(list(uppercase_names))  # Output: ['DISHANT', 'RAJPUT', 'SAKSHI', 'SHIDDI']

8. Calculate the Squares of Numbers
Given a list of integers, calculate the square of each number using the map() function and represent in dict.
Solution:
numbers = [2, 3, 4, 5]
squares = map(lambda num: (num,num ** 2), numbers)
print(dict(squares))  # Output: {2:4, 3:9, 4:16, 5:25}

9. Add Corresponding Elements from Two Lists
Given two lists of equal length, add their corresponding elements using map().

Solution:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_lists = map(lambda x, y: x + y, list1, list2)
print(list(sum_lists))  # Output: [5, 7, 9]

10. Extract the Length of Each String
Given a list of strings, find the length of each string using map().

Solution:
words = ["ragini", "samruddhi", "shiddi", "shyam"]
lengths = map(lambda x: len(x), words)
print(list(lengths))  # Output: [6, 9, 6, 5]


11.Given a list of numbers, calculate the product of all the elements using reduce().

Solution:
from functools import reduce
nums = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 120

12.Given a list of numbers, find the maximum number using reduce().

Solution:
from functools import reduce

nums = [10, 45, 23, 78, 34]
max_num = reduce(lambda x, y: x if x > y else y, nums)
print(max_num)  # Output: 78

13.Given a list of strings, concatenate them into a single string using reduce().
Solution:
from functools import reduce

words = ["Python", "is", "fun"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # Output: "Python is fun"
=================ThankYou==============

"Just like the filter() function sifts out the best from the rest, focus on what truly adds value to your life and let go of the unnecessary."


'''