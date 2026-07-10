#----tuple

#1.tuple is a collection of element which is comma seprated value element within ( ).
    #eg. num=(10,20,30,40)
    #print(type(num))

#2.tuple is a ordered and immutable
#3.tuple is a heteregenious data collection
    # x=(10,20,30,'ravi',[1,2,3],(101,102,103))
#4.Dublicate are allowed in tuple
    # t=(10,20,30,30,40,50,20)
    # print(t)
    # print(type(t))

#======== .count()method=========
# used to count number of times repeated element in the tuple  

# t=(10,20,30,40,50,60,10,20,30,30,40,50,20)
# print(t.count(20))


#======== .index()method=========
# used to get index value of provided element by default value is 0 

# t=(10,20,30,40,50,60,10,20,30,30,40,50,20)
# print(t.index(20,5))


# l=[] #for creating the list square bracket is mandentery.
# print(type(l))

# p=(12,) #for creating a tuple using single value we can use , comma after the element. 
# print(type(p))
# p=12, # you can create a tuple using without parasynthesis. 
# print(type(p))

#get size of a list and tuple by import getsixeof 
# l1=[10,20,30]
# t1=(10,20,30)
# from sys import getsizeof
# print(getsizeof(l1))  #88
# print(getsizeof(t1))  #64



# from sys import getsizeof
# #ex:1
# l1=[1,2,3,4,5,6,7,8,9,10]
# r=range(1,11,1)
# print(getsizeof(l1)) #here list as well as their list element also get the memory space in the memory 
# print(getsizeof(r))   # but in the range only the object can get the memory space in the memory

#ex:2
# l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# r=range(1,21,1)
# print(getsizeof(l1)) #here list as well as their list element also get the memory space in the memory 
# print(getsizeof(r))  # but in the range only the object can get the memory space in the memory