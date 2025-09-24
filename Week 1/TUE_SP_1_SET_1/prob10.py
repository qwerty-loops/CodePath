def split_haycorns(quantity):
	divisor = []
	if quantity == 1:
		return [1]
        
	else:
            for i in range(1,quantity+1):
                if quantity %i==0:
                      divisor.append(i)
            return divisor

			


quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))