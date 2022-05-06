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