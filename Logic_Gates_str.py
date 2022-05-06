from Gates import Gates
from Table_Function import table_gen ; from Validation_Function import validate_and_convert
counter = 0 ; gate_count = ' ' ; POINTS = ['A =','B =','C =','P =','Q =','R =','S =','T =','U =','V =','W =','X =']

print("\nWelcome to our logic gates project, if you haven't already, please check out our GitHub for instructions")
print('https://github.com/YLokma/Logic_Gates \n')
Table = table_gen()
while type(gate_count) != int or gate_count < 1:
	try: gate_count = int(gate_count)
	except ValueError: gate_count = input('\nEnter the number of gates \n')
for point in Table:
	if counter < gate_count:
		print(' ')
		for i in range(3 + counter):
			print(POINTS[i],Table[i])
		print(' ')
		print('Enter the small statement in the form (N GATE M) or (NOT N)')
		if counter == gate_count - 1:
			small_statement = input('X = ').upper()
		else:	
			small_statement = input(POINTS[counter + 3] + ' ').upper()
		small_statement = validate_and_convert(str,small_statement,counter)
		Table.append(Gates[small_statement[1]](Table[small_statement[0]-1],Table[small_statement[2]-1]))
		counter += 1
print('\nX =', Table[-1], '\n')
exit = input('Press enter to exit \n')
