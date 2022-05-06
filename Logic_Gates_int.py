from Gates import Gates ; from Table_Function import table_gen ; from Validation_Function import validate_and_convert ; counter = 0 ; gate_count = ' '

print("\nWelcome to our logic gates project, if you haven't already, please check out our GitHub for instructions")
print('https://github.com/YLokma/Logic_Gates \n')
inputs_no = ' '
while type(inputs_no) != int or inputs_no < 1:
	try: inputs_no = int(inputs_no)
	except ValueError: inputs_no = input('Enter the number of inputs \n')
Table = table_gen(inputs_no)
while type(gate_count) != int or gate_count < 1:
	try: gate_count = int(gate_count)
	except ValueError: gate_count = input('Enter the number of gates \n')
for point in Table:
	if counter < gate_count:
		print(' ')
		for i in range(0,len(Table)):
			print(i+1,'=',Table[i])
		print('\nChoose the gates from')
		print('0:NOT  1:AND  2:OR  3:NAND  4:NOR  5:XOR')
		print('Enter the small statement in the form (123) where 2 is the gate or (01) for NOT 1')
		small_statement = str(input(str(inputs_no + counter + 1) + ' = '))
		small_statement = validate_and_convert(int,small_statement,counter,inputs_no)
		Table.append(Gates[small_statement[1]](Table[small_statement[0]-1],Table[small_statement[2]-1]))
		counter += 1
print('\nX =', Table[-1])
exit = input('\nPress enter to exit \n')
