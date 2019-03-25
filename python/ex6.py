def fact(a):
	if(a==1 or a==0):
		return 1
	else:
		return a*fact(a-1)

a = int(input("enter the value\t"))

p = fact(a)

print(p)

