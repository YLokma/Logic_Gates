from Functions import table_gen,numerically_validate,statement_validation,Gates

inputs_no = numerically_validate('number of inputs')
gate_count = numerically_validate('number of gates')
Table = table_gen(inputs_no) ; counter = 0
while counter < gate_count:
	print(' ')
	for i in range(0,len(Table)):
		print(i+1,'=',Table[i])
	print('\nChoose the gates from')
	print('0:NOT  1:AND  2:OR  3:NAND  4:NOR  5:XOR')
	print('Enter the small statement in the form (123) where 2 is the gate or (01) for NOT 1')
	if counter == gate_count - 1:
		small_statement = input('X = ')
	else:
		small_statement = input(str(inputs_no + counter + 1) + ' = ')
	small_statement = statement_validation(1,small_statement,counter,inputs_no)
	Table.append(Gates[small_statement[1]](Table[small_statement[0]-1],Table[small_statement[2]-1]))
	counter += 1