Tuple are just like list but it is immmutable its value wont change 
written in round brackets
mytuple = (1,2,3)

Dict - Python dictionaries are written with curly brackets, and they have keys and values
mydict  = {"name":"midhun","age":23}

mydict ['name'] #this will return value of key name
get() is another method to return the value of a key
mydict.get('name')

#changing value of a key 
mydict['name'] this will return value of the key 'name' , if you want to 
change the value of 'name' to 'Hari'
mydict['name'] = 'Hari'

#looping through the key, value of dict 
for (key,value) in mydict.items():
	print (key,value)

#adding extra items to the current dict 
ie, if you want to add a new key 'phone-no' to a dict 
mydict['phone-no'] = 9946810526

#removing a key 
mydict.pop("name")
del mydict["name"]

