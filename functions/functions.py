"block of organized, reusable code"


def function_name ():
	pass
"this is the basic structure of a function "
"def is followed by the function name and parentheses ()"
"Argument should be placed inside the parentheses"

def name(name):
	print(name)

name("midhun") #function call
#the output will be 
midhun

#write a function two add 2 nos

def sum(a,b):
	s =  a+b
	return s

a = int(input()) #taking input from user to variable a 
b = int(input()) #taking input from user to variable b
p = sum(a,b) #calling function sum and output wil retunr to variable p

"Argument passinng"
#-----------------------------
"Required arguments"

def sum(a,b):
	s =  a+b
	return s


sum(4)
"while calling sum function it will return error"
TypeError: sum() missing 1 required positional argument: 'b'


#keyword argument concept
#example



def student(name,age):
	print("his name is {}".format(name))
	print("his age is {}".format(age))


student(age=23,name="midhun")
#rather than the position it is focusing on the keyword
#the ouput will be
his name is  midhun
his name is 23



#default argument
"we can set a default value to an argument if the argument is not passing in function call"
def student(name, age, div="b"):
	print("his name is {}".format(name))
	print("his age is {}".format(age))
	print("his age is {}".format(div))

student(age=23,name="midhun")
student(age=23,name="midhun",div ="c")
#check output 

#*args
"suppose we want to pass more argument than we declared in the function definition"
"in such cases we use *args"

def student(name,age,*ss):
	print("his name is {}".format(name))
	print("his age is {}".format(age))
	print(type(ss))


student(age=23,name="midhun")

#the ouput will be 
his name is midhun
his age is 23
<class 'tuple'>


def names(*args):
    for i in args:
        print(i)
        

names(1,2,3,4)
#the ouptu will be
1
2
3
4


def names(firstno,*args):
	print("the first number is ",firstno)
	for i in range(len(args)):
		print("elements in the args at {0} th position is {1}".format(i,args[i]))

names(1,2,3,4,5,6,7)

#the output will be
the first number is  1
elements in the args at 0 th position is 2
elements in the args at 1 th position is 3
elements in the args at 2 th position is 4
elements in the args at 3 th position is 5
elements in the args at 4 th position is 6
elements in the args at 5 th position is 7

#**kwargs
"suppose we want to pass more keyword argument than we declared in the function definition"
"in such cases we use **args"
def student(name,**args):
    print(name)
    print(args)
    
student("midhun",age=2,college="CETkr")
#theoutput will be
midhun
{'age': 2, 'college': 'CETkr'}
