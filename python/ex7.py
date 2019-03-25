def fibonacy(n):
	if n<=1:
		return n
	else:
		return(fibonacy(n-1) + fibonacy(n-2))

a=int(input("enter the value\t"))

for i in range(a):
	print(fibonacy(i))