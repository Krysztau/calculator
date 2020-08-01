
ans= float (input("First number: "))
next_number = 1
while next_number != '' :
	if next_number == '0' :
		next_number = (input("Choose a different number:(not zero) "))
		continue
	else :
		ans /= float (next_number)
		next_number = (input("Next number: "))
if ans == int (ans) :
	ans = int (ans)
ans = round (ans ,12)
print ('Total =', ans )



