#try-except-finally
"try is used to test the code"
"except is used to handle the error"
"finally lets you to execute the code"

#example
no = 25
try:
	no.strip()
except:
	print("sorry it is not a no")

"here the error will execute if it is not defined in the try block"
#strip is the property of srting 

#excepting more exception

no = 25
try:
	no.strip()
except AttributeError:
	print("it is an AttributeError")
except:
	print("sorry")

#'int' object has no attribute 'strip' it is an attribute error so except Attributeerror will occur first
the output will be "it is an AttributeError"

#finally
"finally block will execute what ever the output of try block"
no = 25 
try: 
	no.strip() 
except AttributeError: 
	print("it is an AttributeError") 
finally: 
    print("executed") 
    
"raise is used to throw an exception"
no = 25
if (type(no)!=str): 
    raise TypeError("sorry it is not string and can not do strip") 
                                                   
