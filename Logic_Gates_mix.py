from Functions import *

inputs_no = numerically_validate('number of inputs')
gate_count = numerically_validate('number of gates')
Table = table_gen(inputs_no)
counter = 0
while counter < gate_count:
	print(' ')
	for i in range(0,len(Table)):
		print(i+1,'=',Table[i])
	print(' ')
	print('Enter the small statement in the form (N GATE M) or (NOT N), where N & M are numbers')
	if counter == gate_count - 1:
		small_statement = input('X = ').upper()
	else:
		small_statement = input(str(inputs_no + counter + 1) + ' = ').upper()
	small_statement = statement_validation(2,small_statement,counter,inputs_no)
	Table.append(Gates[small_statement[1]](Table[small_statement[0]-1],Table[small_statement[2]-1]))
	counter += 1