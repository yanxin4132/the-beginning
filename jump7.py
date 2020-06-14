i = 0
while i <=99:
	i+=1
	a = str(i)
	if i%7 == 0:
		continue
	elif a[0] == "7":
		continue
	elif i>10 and a[1] == "7":
		continue
	else:
		print(i)
