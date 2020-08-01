print ("Welcome to calculator plus")
a= float (input("First number: "))
b= float (input("Second number: "))
c= b+a
if c == int (c) :
	c= int (c)
c= round (c ,12)
print (a, '+', b, '=', c)