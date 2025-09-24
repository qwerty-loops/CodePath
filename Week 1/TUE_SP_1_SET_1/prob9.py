def can_pair(item_quantities):
	if len(item_quantities) == 0:
		return True
	else:
		pair =0
		for i in item_quantities:
			if i%2!=0:
				return False
			elif i%2 == 0:
				pair +=1
				if pair == len(item_quantities):
					return True

item_quantities = [2, 4, 6, 9]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))