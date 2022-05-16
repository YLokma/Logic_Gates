from Functions import *

Table = table_gen()
counter = 0
gate_count = numerically_validate('number of gates',9)
POINTS = ['A =','B =','C =','P =','Q =','R =','S =','T =','U =','V =','W =','X =']
while counter < gate_count:
	print(' ')
	for i in range(3 + counter):
		print(POINTS[i],Table[i])
	print(' ')
	print('Enter the small statement in the form (N GATE M) or (NOT N)')
	if counter == gate_count - 1:
		small_statement = input('X = ').upper()
	else:
		small_statement = input(POINTS[counter + 3] + ' ').upper()
	small_statement = statement_validation(3,small_statement,counter)
	Table.append(Gates[small_statement[1]](Table[small_statement[0]-1],Table[small_statement[2]-1]))
	counter += 1