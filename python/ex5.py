#itrations using comprehension list
h_letters = [ letter for letter in 'human' ]
print(h_letters)

#nested if statements in comprehension list
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print('\n',num_list)

#if else statement in comprehension list

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print('\n',obj)

#transpose of matrix comprehension list

matrix = [[1, 2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print ('\n',transpose)

# comprehension list for dictionary
def eg3_lc(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }

country = ['India', 'Pakistan', 'Nepal', 'Bhutan', 'China', 'Bangladesh']
capital = ['New Delhi', 'Islamabad','Kathmandu', 'Thimphu', 'Beijing', 'Dhaka']

print ("\nLC result      : ",str(eg3_lc(country, capital)))
