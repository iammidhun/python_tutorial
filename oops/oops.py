-----------------
object
object is an real word entity 
for example student , office , pen etc..

object has attribute and behaviour

for example student is an object , it has attribute "name", "age"
the functions that he does is his behaviour na?

class 
"class is a group of object"

syntax 

class classname():
	def __init__():
	......................................
	...............................
	......................................


class Student:
	def __init__(self,name,age):
		self.name =  name #self means an object
		self.age = age 

obj =  Student("midhun",23) #an instance created of the class Student
ob.name #this will return name
"midhun"
#__init__ is a special Python method that is automatically called when memory is allocated for a new object
# The sole purpose of __init__ is to initialize the values of instance members for the new object


"class attribute"

class Student:
	div = "B" #div is a class attribute
	def __init__(self,name,age):
		self.name = name
		self.age  =  age

"class attribute  is common for any object and attributes passed in __init__ is only for particular object"
