# def Split(mix):
# 	even = []
# 	odd = []
# 	for i in mix:
# 		if (i % 2 == 0):
# 			even.append(i)
# 		else:
# 			odd.append(i)
# 	print ("Print the even number: ", even)
# 	print ("Print the odd number: ", odd)

mix = [1,2,4,5,9,11,15,8,6]
# Split(mix)

even = [i for i in mix if i % 2 == 0]
print (even)

odd = [i for i in mix if i % 2 != 0]
print (odd)