
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

#an if statement is written by using if keyword

name  =  "midhun"
if (name=='midhun'):
	print ("okay his name is correct")

#if-else 

if (name!='hari'):
	print ('sorry you have entered a wrong name')
else :
	print('you have entered correct name')

#nested if 

x = input("enter a no ") #accepting an input from user
x = int(x) #converting string to int
if (x<30):
	print ("x is less than 30")
	if (x<20):
		print("x is less than 20")
		if (x<15):
			print("x is less than 15")

#using pass
"when you want to make a condition to be empty you can simply add pass statemnt inside it"
if (5<4):
	pass

#foor loop 
iterating over list , tuple, string , dictionary etc

for is the keyword

#for example
students  = [1,2,3,4,5,6,7,8,9,10]

for i in students:
	print (i)

"this will print each oject of the list students"

for i in "midhun":
	print (i)
"the output will be each letter of the string 'midhun'"