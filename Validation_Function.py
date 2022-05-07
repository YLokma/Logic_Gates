gates_dict = {'NOT':0,'AND':1,'OR':2,'NAND':3,'NOR':4,'XOR':5} ; points_dict = {'A':1,'B':2,'C':3,'P':4,'Q':5,'R':6,'S':7,'T':8,'U':9,'V':10,'W':11}
points_and_gates = {'A':1,'B':2,'C':3,'P':4,'Q':5,'R':6,'S':7,'T':8,'U':9,'V':10,'W':11,'NOT':0,'AND':1,'OR':2,'NAND':3,'NOR':4,'XOR':5}

def validate_and_convert(file:type, small_statement, counter:int,inputs_no:int = 3)  -> list:
	while counter + inputs_no > 9 and ' ' not in small_statement and len(small_statement) > 3:
		small_statement = input('You have to insert spaces now \n')
	if ' ' in small_statement:
		small_statement = small_statement.split(' ')
	else:
		small_statement = list(small_statement)
	if len(small_statement) == 2:
				small_statement.insert(0,small_statement[1])
	if file == str:	
		while len(small_statement) != 3 or small_statement[1] not in gates_dict or small_statement[0] not in points_dict or small_statement[2] not in points_dict:
				small_statement = input('Re-enter the small statement in the form (N GATE M) or (NOT N) \n').upper()
				if ' ' in small_statement:
					small_statement = small_statement.split(' ')
				else:
					small_statement = list(small_statement)
				if len(small_statement) == 2:
					small_statement.insert(0,small_statement[1])
		for i in range(len(small_statement)):
			small_statement[i] = points_and_gates[small_statement[i]]
	elif file == int:
		for i in range(len(small_statement)):
			small_statement[i] = int(small_statement[i])
	while len(small_statement) != 3 or small_statement[0]-1 not in range(inputs_no + counter) or small_statement[2]-1 not in range(inputs_no + counter) or small_statement[1] not in range(0,5+1) or (small_statement[0] == small_statement[2] and small_statement[1] != 0):
		small_statement = input('Invalid statement, please re-enter the small statement correctly \n').upper()
		if ' ' in small_statement:
			small_statement = small_statement.split(' ')
		else:
			small_statement = list(small_statement)
		if len(small_statement) == 2:
				small_statement.insert(0,small_statement[1])
		if file == str:
			for i in range(len(small_statement)):
				small_statement[i] = points_and_gates[small_statement[i]]
		elif file == int:
			for i in range(len(small_statement)):
				small_statement[i] = int(small_statement[i])
	return small_statement
