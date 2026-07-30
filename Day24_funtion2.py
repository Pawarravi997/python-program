#function is a reusable block of code.its used to avoid repeating code. function is only once we define the function you can used multiple times in the programes 

#else is used with the for loop. else will execute after for loop excute completely, if break statement is present they will does not execute the else bz they will break whole for loop.

# #wap to reverse the word

# def reverse(word):
#     name=''
#     for wrd in word:
#         name=wrd+name
#     print(name)    
# reverse('ravi')    



# #wap to reverse sentence at place

# def reverse(sen):
#     words=sen.split()
#     rev_word=[]
#     for word in words:
#         rev=''
#         for char in word:
#             rev=char+rev
#         rev_word.append(rev)
#     result=' '.join(rev_word)        
#     print(result)    
# reverse('the kiran academy')        


# def search(sen,word):
#     words=sen.split()
#     for wd in words:
#         if wd==word:
#             print('yes')
#             break
#     else:
#          print('no')  
# search('python is a simple programming language','pyhton')  

# def search(sen,name):
#     word=sen.split()
#     for  wd in word:
#         if wd==name:
#             print("yes")
#             break
#     else:
#         print("no")
# search("python is a smiple dynamic programming language","python")   


# num=123456
# rev=0
# while num>0:
#   digit=num%10
#   print(digit)
#   rev=rev*10+digit
#   num=num//10
# print(rev) 



# def reverse(name):
#     rev=""
#     for char in name:
#         rev=char+rev
#     print(rev)
# reverse("gitanjali") 


# def function(sen):
#     words=sen.split()
#     rev_word=[]
#     for word in words:
#         rv=''
#         for char in word:
#             rv=char+rv
#         rev_word.append(rv)
#     result=' '.join(rev_word)
#     print(result)
# function("my name is akshay")  







