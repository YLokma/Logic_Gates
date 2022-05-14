# Statement Validation
gates_dict = {'NOT':0,'AND':1,'OR':2,'NAND':3,'NOR':4,'XOR':5} ; points_dict = {'A':1,'B':2,'C':3,'P':4,'Q':5,'R':6,'S':7,'T':8,'U':9,'V':10,'W':11}
points_and_gates = {'A':1,'B':2,'C':3,'P':4,'Q':5,'R':6,'S':7,'T':8,'U':9,'V':10,'W':11,'NOT':0,'AND':1,'OR':2,'NAND':3,'NOR':4,'XOR':5} 

def statement_validation(file:str,small_statement ,counter:int,inputs_no:int = 3)  -> list:
	while counter + inputs_no > 9 and ' ' not in small_statement and len(small_statement) > 3:
		small_statement = input('You have to insert spaces \n')
	if ' ' in small_statement:
		small_statement = small_statement.split()
	else:
		small_statement = list(small_statement)
	if len(small_statement) == 2:
		small_statement.insert(0,small_statement[1])
	if file == 'str':	
		while len(small_statement) != 3 or small_statement[1] not in gates_dict or small_statement[0] not in points_dict or small_statement[2] not in points_dict:
				small_statement = input('Re-enter the small statement in the form (N GATE M) or (NOT N) \n').upper().split()
				if len(small_statement) == 2:
					small_statement.insert(0,small_statement[1])
		for i in range(len(small_statement)):
			small_statement[i] = points_and_gates[small_statement[i]]
	elif file == 'mix':
		while len(small_statement) == 1 or small_statement[1] not in gates_dict:
			small_statement = input('Re-enter the small statement in the form (N GATE M) or (NOT N) \n').upper().split()
			if len(small_statement) == 2:
				small_statement.insert(0,small_statement[1])
		small_statement[1] = gates_dict[small_statement[1]]
		for i in range(len(small_statement)):
			small_statement[i] = int(small_statement[i])
	elif file == 'int':
		for i in range(len(small_statement)):
			small_statement[i] = int(small_statement[i])
	while len(small_statement) != 3 or small_statement[0]-1 not in range(inputs_no + counter) or small_statement[2]-1 not in range(inputs_no + counter) or small_statement[1] not in range(0,5+1) or (small_statement[0] == small_statement[2] and small_statement[1] != 0):
		small_statement = input('Invalid statement, please re-enter the small statement correctly \n').upper()
		if ' ' in small_statement:
			small_statement = small_statement.split()
		else:
			small_statement = list(small_statement)
		if len(small_statement) == 2:
				small_statement.insert(0,small_statement[1])
		if file == 'str':
			for i in range(len(small_statement)):
				small_statement[i] = points_and_gates[small_statement[i]]
		elif file == 'mix':
			while small_statement[1] not in gates_dict:
				small_statement = input('Re-enter the small statement in the form (N GATE M) or (NOT N) \n').upper().split()
			small_statement[1] = gates_dict[small_statement[1]]
			for i in range(len(small_statement)):
				small_statement[i] = int(small_statement[i])
		elif file == 'int':
			for i in range(len(small_statement)):
				small_statement[i] = int(small_statement[i])
	return small_statement

# Numerical Input Validation
from json.encoder import INFINITY

def numerically_validate(variable_name:str ,maximum:int = INFINITY , minimum:int = 1) -> int:
    variable = ' '
    while type(variable) != int:
        try: variable = int(variable)
        except ValueError: variable = input(f'Enter the {variable_name} \n')
    while variable < minimum or variable > maximum:
        variable = ' '
        while type(variable) != int:
            try: variable = int(variable)
            except ValueError: variable = input(f'Invalid {variable_name} \n')
    return variable 

# Gates

def not_gate(wire1:list,wire2=[]):
    wire_out = []
    for i in range(len(wire1)):
        if wire1[i] == 1: wire_out.append(0)
        else: wire_out.append(1)
    return wire_out

def and_gate(wire1:list,wire2:list):
    wire_out = []
    for i in range(0,len(wire1)):
        wire_out.append(wire1[i]*wire2[i])
    return wire_out

def or_gate(wire1:list,wire2:list):
    wire_out = []
    for i in range(len(wire1)):
        wire_out.append(wire1[i]+wire2[i])
        if wire_out[i] > 0: wire_out[i] = 1
        else: wire_out[i] = 0
    return wire_out

def nand_gate(wire1:list,wire2:list):
    return not_gate(and_gate(wire1, wire2))

def nor_gate(wire1:list,wire2:list):
    return not_gate(or_gate(wire1, wire2))

def xor_gate(wire1:list,wire2:list):
    wire_out = []
    for i in range(len(wire1)):
        wire_out.append(wire1[i]+wire2[i])
        if wire_out[i] == 1: wire_out[i] = 1
        else: wire_out[i] = 0
    return wire_out

Gates = [not_gate,and_gate,or_gate,nand_gate,nor_gate,xor_gate]

# Table Generator
def table_gen(inputs_no:int = 3) -> list:
	Table_S = [] ; Table = [[]] ; counter = 0
	for i in range(inputs_no,0,-1):
		Table_S.append(list(('0' * 2**(i-1) + '1' * 2**(i-1)) * 2 ** counter))
		counter+=1
	counter = 0
	for p in Table:
		if counter < inputs_no:
			for q in range(0,2**inputs_no):
				p.append(int(Table_S[counter][q]))
		if counter < inputs_no - 1:
			Table.append([])
		else: break
		counter+=1
	return Table