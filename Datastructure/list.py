 
List - the name indicates , it is a list of objects 
	placing all the items (elements) inside a square bracket [ ], separated by commas
it may contain different types of object 

mylist  = ['1',1]
"diiferent operation on list"

mylist[0] = 1

mylist = [1,2,3,4,5,6,7,8,9]
mylist[0:2] = [1,2] #list slicing
mylist[-1] = 9  

#list value can be changed using '=' 
mylist[0]= 9
"now mylist will be "
mylist = [9,2,3,4,5,6,7,8,9]

#use append() to add element and use extend to append multiple items at the end position

mylist.append(1)
mylist.extend('1','2')


#to insert an element at any position that you want, use insert()

mylist.insert(index,value)
for example to insert 9 to 2nd index 
mylist.insert(2,9)

#to delete a list or to delete single or multiple elemets from a list use del
del mylist[0]
del mylist[0:2]
del mylist

#to remove a particular element use remove 
#to remove last element use pop 
mylist.remove(9) #it will remove 9 from the first position
mylist.pop() #it will remove last element of that list


mylist.count(1)
it will return occurance of 1 in mylist

sort is used to sort the list 
and reverse is used to reverse the sort 