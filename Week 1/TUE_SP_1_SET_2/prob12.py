def shuffle(cards):
	nc =[]
	l=len(cards)
	n=l//2
	l1=cards[:n]
	l2=cards[n:]
	for i in range(n):
		nc.append(l1[i])
		nc.append(l2[i])
	return nc
		


cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))