#---Dict

#dict is a key and value pair within a curly braces { }
#syntax....var_name={key1:value1,key2:value2.........}
#it must be immutable and unique


# details={"roll_no":1,"name":"ravi","city":"pune"}
# print(type(details))

# sqr={1:1,2:4,3:9,4:16,5:25,6:36}
# print(type(sqr))

#create dict to represent course details 
# detail={'c_name':"data science","c_duration":"6 month","fees":30000,"teacher":"vaibhav sir"} #alt+z used to wrap word
# print(detail)
# print(type(detail))

#create a dict to represent cube of numbers from 11-15
# cube={11:11**3,12:12**3,13:13**3,14:14**3,15:15**3}
# print(cube)
# if you are provide duplicate it will be overwrite on first value or update first value with duplicate value

#--key:
   # immutable and UNIQUE

# mark={1:89,2:45,3:99}
# print(mark)

# result={"English":"pass","hindi":"pass","marathi":"fail"}
# print(type(result))
# print(result)

# name={1.1:"ravi",1.2:"radha",1.2:"kiran",(1.4,):23}
# print(type(name))
# print(name)

#--value:
   #mutable/immutable---duplicate

# details={"roll":25,"name":"ravi","height":5.78,"courses":["python","java"],"age":25,"marks":{"python":98,"java":88}}
# print(type(details))
# print(details)


#create a dict to represent state and capital
# details={"maharashtra":"mumbai","bihar":"patna","west bangal":"kolkatta","telengana":"hydrabad","punjab":"chandigarh","himachal pradesh":"shimla"}
# print(type(details))
# print(details)


#create a dict to represent language and their founder
# details={"python":"Guido van Rossum","sql":{"founder name":"Donald D. Chamberlin","founder name 2" :"Raymond F. Boyce"}}
# print(details)


#create a dict to represent single employee details:
#ex:1
# ravi_details={"city":"pune","salary":50000}
# print(ravi_details)

#ex:2
# details={"name":"ravi","percentage":89.67}
# print(details)

#nested dict example
#ex:1
# placement_details={101:{"empname":"ravi","salary":"500000"},102:{"empname":"rahul","salary":70000}}
# print(placement_details)

#ex:2
# batch_1336={1:{"name":"ravi","percentage":89.90},2:{"name":"rohit","percentage":90,3:{"name":"raja","percentage":99}}}
# print(batch_1336)

#ex:3
# tka={"placement":{"p101":{"name":"ravi","salary":60000},"p102":{"name":"rahul","salary":80000}},"sells":{"s101":{"name":"radha","salary":70000},"s102":{"name":"kishor","salary":"60000"}}}
# print(tka)

#ex:4
# movie_details={"STK":{"actor":"harshvardhan","actress":"mawra","director":" Radhika rao","producer":"deepak mukut"}}
# print(movie_details)

#ex:5
# python_batches={1336:{"id101":{"name":"ravi"},"id102":{"name":"khushal"}},1335:{"id101":{"name":"rahul"},"id102":{"name":"pankaj"}}}
# print(python_batches)

# #ex:6
# India={"s1":{"d":['sd1','sd2','sd3']},"s2":{"d2":["sb1","sb2","sd3"]},"s3":{"d":["sb1","sb2","sd3"]}}

# country={"s1":{"d":['sd1','sd2','sd3']}}

#using key get value of that key ---code with harry
# dictt={'apple':'saparchand',"skin":"twacha"}
# word=(input('enter knoe meaning of that word:'))
# print(dictt[word])