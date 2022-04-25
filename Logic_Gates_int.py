from Gates import Gates ; from Dynamic_Table import Table, inputs_no ; counter = 0
gate_count = str
while type(gate_count) != int:
	try: gate_count = int(input('Enter the number of gates \n'))
	except ValueError: gate_count = int(input('Invalid number of gates, try again \n'))
	continue
while gate_count < 1 or gate_count > 9:
	gate_count = int(input('Invalid number of gates, try again \n'))
for point in Table:
	if counter < gate_count:
		turn = str(counter + inputs_no + 1) + '='
		print('Enter the small statement in the form (N GATE M) or (NOT N)')
		print('Choose the gates from')
		print('0:NOT \t 1:AND \t 2:OR \t 3:NAND \t 4:NOR \t 5:XOR')
		if counter == gate_count - 1:
			small_statement = str(input('X = '))
		else:	
			small_statement = str(input(str(counter + inputs_no + 1) + ' = '))		
		small_statement = small_statement.split()
		if len(small_statement) == 1:
			if small_statement[0][0] == '0':
				for i in range(0,2):
					small_statement.append(int(small_statement[0][i]))
			else:
				for i in range(0,3):
					small_statement.append(int(small_statement[0][i]))
			small_statement.pop(0)
		elif len(small_statement) > 1:
			for i in range(0, len(small_statement)):
				small_statement[i] = int(small_statement[i])
		if len(small_statement) == 2:
			while small_statement[0] != 0:
				print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
				print('Choose the gates from')
				print('0:NOT \t 1:AND \t 2:OR \t 3:NAND \t 4:NOR \t 5:XOR')
				if counter == gate_count - 1:
					small_statement = str(input('X = '))
				else:	
					small_statement = str(input(str(counter + inputs_no + 1) + ' = '))	
				small_statement = small_statement.split()
				for i in range(0,2):
					small_statement.append(int(small_statement[0][i]))
				small_statement.pop(0)
			while small_statement[1]-1 not in range(0,len(Table)):
				print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
				print('Choose the gates from')
				print('0:NOT \t 1:AND \t 2:OR \t 3:NAND \t 4:NOR \t 5:XOR')
				if counter == gate_count - 1:
					small_statement = str(input('X = '))
				else:	
					small_statement = str(input(str(counter + inputs_no + 1) + ' = '))	
				small_statement = small_statement.split()
				for i in range(0,3):
					small_statement.append(int(small_statement[0][i]))
				small_statement.pop(0)
		else:
			while small_statement[1] > 5 or small_statement[1] < 0:
				print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
				print('Choose the gates from')
				print('0:NOT \t 1:AND \t 2:OR \t 3:NAND \t 4:NOR \t 5:XOR')
				if counter == gate_count - 1:
					small_statement = str(input('X = '))
				else:	
					small_statement = str(input(str(counter + inputs_no + 1) + ' = '))	
				small_statement = small_statement.split()
				for i in range(0,3):
					small_statement.append(int(small_statement[0][i]))
				small_statement.pop(0)
			while small_statement[0]-1 not in range(0,len(Table)) or small_statement[2]-1 not in range(0,len(Table)):
				print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
				print('Choose the gates from')
				print('0:NOT \t 1:AND \t 2:OR \t 3:NAND \t 4:NOR \t 5:XOR')
				if counter == gate_count - 1:
					small_statement = str(input('X = '))
				else:	
					small_statement = str(input(counter + gate_count))
				small_statement = small_statement.split()
				for i in range(0,3):
					small_statement.append(int(small_statement[0][i]))
				small_statement.pop(0)
		Table.append([])		
		for i in range(0,2**inputs_no):
			if len(small_statement) == 3:
				if small_statement[1] == 0:
					Table[-1].append(Gates[small_statement[1]](Table[small_statement[0]-1][i]))
				else:	
					Table[-1].append(Gates[small_statement[1]](Table[small_statement[0]-1][i],Table[small_statement[2]-1][i]))
			elif len(small_statement) == 2:
				Table[-1].append(Gates[small_statement[0]](Table[small_statement[1]-1][i]))
			else: 
				print('Error')
				break
		print('')
		if counter < gate_count - 1:
			for i in range(0,len(Table)):
				print(i+1,'=',Table[i])
		else:
			for i in range(0,len(Table)-1):
				print(i+1,'=',Table[i])
		print('')
	else: break
	counter += 1
print('\t\t X = ', Table[-1], '\n')
