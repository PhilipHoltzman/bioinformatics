#! Python 3

# Counting Point Mutations using the Hamming Distance



# initial data
s = ''
t = ''

# splitting the data into individual letters
s = list(s)
t = list(t)

# Hamming Distance Var
hDistance = 0
# counting var
n = 0

# matching algorithm 
for i in s:
	if i == t[n]:
		print('match')
		n = n + 1

	else:
		print('no match')
		n = n + 1
		hDistance = hDistance + 1

# print solution
print(hDistance)

	

	
