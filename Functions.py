# Statement Validation
gates_dict = {'NOT':0,'AND':1,'OR':2,'NAND':3,'NOR':4,'XOR':5} ; points_dict = {'A':1,'B':2,'C':3,'P':4,'Q':5,'R':6,'S':7,'T':8,'U':9,'V':10,'W':11}
int_gates_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5}; int_points_dict = {} ; all_gates = [0,int_gates_dict,gates_dict,gates_dict]

def statement_validation(input_type:int,small_statement ,counter:int,inputs_no:int = 3) -> list:
	for i in range(len(int_points_dict)+1,inputs_no+counter+1):
		int_points_dict[str(i)] = i
	all_points = [0,int_points_dict,int_points_dict,points_dict]
	while counter + inputs_no > 9 and ' ' not in small_statement and len(small_statement) > 3:
		small_statement = input('You have to insert spaces \n').upper()
	if ' ' in small_statement:
		small_statement = small_statement.split()
	else:
		small_statement = list(small_statement)
	if len(small_statement) == 2:
		small_statement.insert(0,small_statement[1])
	while len(small_statement) != 3 or small_statement[1] not in all_gates[input_type] or small_statement[0] not in all_points[input_type] or small_statement[2] not in all_points[input_type]:
		small_statement = input('Re-enter the small statement correctly \n').upper()
		if ' ' in small_statement:
			small_statement = small_statement.split()
		else:
			small_statement = list(small_statement)
		if len(small_statement) == 2:
			small_statement.insert(0,small_statement[1])
	small_statement[0] = all_points[input_type][small_statement[0]]
	small_statement[1] = all_gates[input_type][small_statement[1]]
	small_statement[2] = all_points[input_type][small_statement[2]]
	while len(small_statement) != 3 or small_statement[0]-1 not in range(inputs_no + counter) or small_statement[2]-1 not in range(inputs_no + counter) or (small_statement[0] == small_statement[2] and small_statement[1] != 0):
		small_statement = input('Invalid statement, please re-enter the small statement correctly \n').upper()
		if ' ' in small_statement:
			small_statement = small_statement.split()
		else:
			small_statement = list(small_statement)
		if len(small_statement) == 2:
			small_statement.insert(0,small_statement[1])
		small_statement[0] = all_points[input_type][small_statement[0]]
		small_statement[1] = all_gates[input_type][small_statement[1]]
		small_statement[2] = all_points[input_type][small_statement[2]]
	return small_statement

# Numerical Input Validation
from json.encoder import INFINITY

def numerically_validate(variable_name:str , minimum:int = 1 , maximum:int = INFINITY) -> int:
    variable = input(f'Enter the {variable_name} \n')
    while type(variable) != int:
        try: variable = int(variable)
        except ValueError: variable = input(f'Invalid {variable_name}, try again \n')
    while variable < minimum or variable > maximum:
        variable = ' '
        while type(variable) != int:
            try: variable = int(variable)
            except ValueError: variable = input(f'Invalid {variable_name}, try again \n')
    return variable

# Gates

def not_gate(wire1:list,wire2=[]) -> list:
    wire_out = []
    for i in range(len(wire1)):
        if wire1[i] == 1: wire_out.append(0)
        else: wire_out.append(1)
    return wire_out

def and_gate(wire1:list,wire2:list) -> list:
    wire_out = []
    for i in range(0,len(wire1)):
        wire_out.append(wire1[i]*wire2[i])
    return wire_out

def or_gate(wire1:list,wire2:list) -> list:
    wire_out = []
    for i in range(len(wire1)):
        wire_out.append(wire1[i]+wire2[i])
        if wire_out[i] > 0: wire_out[i] = 1
        else: wire_out[i] = 0
    return wire_out

def nand_gate(wire1:list,wire2:list) -> list:
    return not_gate(and_gate(wire1, wire2))

def nor_gate(wire1:list,wire2:list) -> list:
    return not_gate(or_gate(wire1, wire2))

def xor_gate(wire1:list,wire2:list) -> list:
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