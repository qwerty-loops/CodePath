def good_pairs(pile1, pile2, k):
	gp=0
	for i,v1 in enumerate(pile1):
		for j,v2 in enumerate(pile2):
			if v1%(v2*k)==0:
				gp+=1
	return gp

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))