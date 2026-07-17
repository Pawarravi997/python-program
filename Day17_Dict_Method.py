'''
dict key is sometime int , float , and string
'''
# details={'name':'ravi','age':26}

#---add
#syntax:var_name[key]=value

# details['city']='pune'
# print(details)   #{'name':'ravi','age':26,'city':'pune}
# details["duration"]='6 month'
# print(details)

#---update
#syntax:var_name.update(parameter/key=value/arg)

# details.update(course='Data analytics',instite='tka')
# print(details)
# details.update(branch="karve nagar")
# print(details)

# details={'name':'ravi','age':26}

#---acess (used to acces the dict element or value using their key)
#syntax:var_name[key]
# print(details['name'])
# print(details['age'])
# print(details['city']) # here they show the key error.

#---get
#syntax:var_name.get(key)
# print(details.get('name'))
# print(details.get('city')) #here print by default none value
# print(details.get('city','no data for city')) #here city is a key value which is used to get the value of that key ,so they dont have any value of them so it will print none . if you provide info after , comma this value print in output

# details={'name':'ravi','age':26}

#--delete:
#var_name.pop(key) #it get key for delete the key and value and return none
#var_name.popitem() #they can delelt last key by default and return a tuple
# print(details.pop('name'))
# print(details.popitem())


# details={'name':'ravi','age':26}
#---update
#syntax:var_name[key]=value
# details['city']='pune'
# print(details)
# details['name']='pune' #here they can overwrite the first value and update them
# print(details)


#----practice
# details={'name':'ravi','age':26}
# details['city']='pune' #add
# print(details)

# details.update(city='pune') #update method
# print(details)
# details.update({'salary':90000}) #update using dict providing
# print(details)

# print(details['age']) #acess

# print(details.pop('name')) #delete key and value and return value
# print(details)
# print(details.popitem()) #delete by default last key and return tuple

# details={'name':'ravi','age':26}

#--copy
# data=details.copy()  #used for copy
# print(data)


# details={'name':'ravi','age':26}
#--key () method -used for getting all key from a dict using this method
# print(details.keys())  #dict_key(['name','age'])

#--value() method -used for get all values from a dict using this method
# print(details.values())  #dict_values(['ravi','26'])

#--items () method -used for getting all key and all values from a dict using this method in a list of tuple form
# print(details.items())  #dict_item[('name','ravi'),('age',26)]

 
