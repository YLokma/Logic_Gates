from Gates import Gates ; from Default_Table import Table ; counter = 0 ; POINTS = ['A = ','B = ','C = ','P = ','Q = ','R = ','S = ','T = ','U = ','V = ','W = ','X = '] 
points_and_gates = {'A':1,'B':2,'C':3,'P':4,'Q':5,'R':6,'S':7,'T':8,'U':9,'V':10,'W':11,'a':1,'b':2,'c':3,'p':4,'q':5,'r':6,'s':7,'t':8,'u':9,'v':10,'w':11, 'NOT':0,'AND':1,'OR':2,'NAND':3,'NOR':4,'XOR':5,'not':0,'and':1,'or':2,'nand':3,'nor':4,'xor':5,'Not':0,'And':1,'Or':2,'Nand':3,'Nor':4,'Xor':5}
gates_dict = {'AND':1,'OR':2,'NAND':3,'NOR':4,'XOR':5,'and':1,'or':2,'nand':3,'nor':4,'xor':5,'And':1,'Or':2,'Nand':3,'Nor':4,'Xor':5} ; NOT = {'NOT','Not','not'}
points_dict = {'A':1,'B':2,'C':3,'P':4,'Q':5,'R':6,'S':7,'T':8,'U':9,'V':10,'W':11,'a':1,'b':2,'c':3,'p':4,'q':5,'r':6,'s':7,'t':8,'u':9,'v':10,'w':11}
print('')
print("Welcome to our logic gates project, if you haven't already, please check out our GitHub for instructions")
print('https://github.com/YLokma/Logic_Gates')
print('')
for i in [0,1,2]:
	print(POINTS[i],Table[i])
print('')
gate_count = str
while type(gate_count) != int:
	try: gate_count = int(input('Enter the number of gates \n'))
	except ValueError: gate_count = int(input('Invalid number of gates, try again \n'))
	continue
while gate_count < 1:
	gate_count = int(input('Invalid number of gates, try again \n'))
for point in Table:
	if counter < gate_count:
		if counter == gate_count - 1:
			print('Enter the small statement in the form (N GATE M) or (NOT N)')
			small_statement = str(input('X = '))
		else:	
			print('Enter the small statement in the form (N GATE M) or (NOT N)')
			small_statement = str(input(POINTS[counter + 3]))
		small_statement = small_statement.split()
		if len(small_statement) == 2:
			while (small_statement[0] not in NOT and len(small_statement) < 3) or small_statement[1] not in points_dict:
				if counter == gate_count - 1:
					print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
					small_statement = str(input('X = '))
				else:	
					print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
					small_statement = str(input(POINTS[counter + 3]))				
				small_statement = small_statement.split()
		if len(small_statement) != 2:
			while len(small_statement) == 1 or len(small_statement) > 3 or small_statement[1] not in gates_dict or small_statement[0] not in points_dict or small_statement[2] not in points_dict:
				if small_statement[0] in NOT: break
				if counter == gate_count - 1:
					print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
					small_statement = str(input('X = '))
				else:	
					print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
					small_statement = str(input(POINTS[counter + 3]))				
				small_statement = small_statement.split()		
		for i in [0,0,0]:
			if type(small_statement[i]) == int: break
			small_statement.append(points_and_gates[small_statement[0]])
			small_statement.pop(0)
		if len(small_statement) == 3:
			while small_statement[0]-1 not in range(0,len(Table)) or small_statement[2]-1 not in range(0,len(Table)):
				if counter == gate_count - 1:
					print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
					small_statement = str(input('X = '))
				else:	
					print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
					small_statement = str(input(POINTS[counter + 3]))				
				small_statement = small_statement.split()
				for i in [0,0,0]:
					if type(small_statement[i]) == int: break
					small_statement.append(points_and_gates[small_statement[0]])
					small_statement.pop(0)
		elif len(small_statement) == 2:
			while small_statement[1]-1 not in range(0,len(Table)):
				if counter == gate_count - 1:
					print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
					small_statement = str(input('X = '))
				else:	
					print('Re-enter the small statement in the form (N GATE M) or (NOT N)')
					small_statement = str(input(POINTS[counter + 3]))				
				small_statement = small_statement.split()
				for i in [0,0,0]:
					if type(small_statement[i]) == int: break
					small_statement.append(points_and_gates[small_statement[0]])
					small_statement.pop(0)
		Table.append([])		
		for i in range(0,8):
			if len(small_statement) == 3:
				if small_statement[1] == 0:
					Table[-1].append(Gates[small_statement[1]](Table[small_statement[0]-1][i]))
				else:	
					Table[-1].append(Gates[small_statement[1]](Table[small_statement[0]-1][i],Table[small_statement[2]-1][i]))
			elif len(small_statement) == 2:
				Table[-1].append(Gates[small_statement[0]](Table[small_statement[1]-1][i]))
			else: 
				print('Error tani')
				break
		print('')
		if counter < gate_count - 1:
			for i in range(0,len(Table)):
				print(POINTS[i],Table[i])
		else:
			for i in range(0,len(Table)-1):
				print(POINTS[i],Table[i])
		print('')
	else: break
	counter += 1
print('\t\t\t X = ', Table[-1], '\n')
