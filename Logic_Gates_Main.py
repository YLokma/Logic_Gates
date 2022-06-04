from Functions import numerically_validate,table_gen,statement_validation,Gates ; from All_Outputs import all_outputs,POINTS

print(all_outputs['Welcome'])
print(all_outputs['Input_Selector'])
input_type = numerically_validate('input type',1,3)
while exit:
	if input_type == 3:
		inputs_no = 3
		gate_count = numerically_validate('number of gates',1,9)
	else:
		inputs_no = numerically_validate('number of inputs')
		gate_count = numerically_validate('number of gates')
	Table = table_gen(inputs_no)
	counter = 0
	while counter < gate_count:
		print(' ')
		for i in range(len(Table)):
			if input_type == 3:
				print(POINTS[i],Table[i])
			else:
				print(i+1,'=',Table[i])
		print(' ')
		print(all_outputs[input_type])
		if counter == gate_count - 1:
			small_statement = input('X = ').upper()
		else:
			if input_type == 3:
				small_statement = input(POINTS[counter + 3] + ' ').upper()
			else:
				small_statement = input(str(inputs_no + counter + 1) + ' = ').upper()
		small_statement = statement_validation(input_type,small_statement,counter,inputs_no)
		Table.append(Gates[small_statement[1]](Table[small_statement[0]-1],Table[small_statement[2]-1]))
		counter += 1
	print(f'\nX = {Table[-1]} \n')
	exit = input(all_outputs['Exit'])
	if exit == '':
		exit = False
	else:
		exit = True