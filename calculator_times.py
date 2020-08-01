
ans= float (input("First number: "))
next_number = 1
while next_number != '' :
	ans *= float (next_number)
	next_number = (input("Next number: "))
	
if ans == int (ans) :
	ans = int (ans)
ans = round (ans ,12)
print ('Total =', ans )



