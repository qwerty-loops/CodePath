def up_and_down(lst):
	en,on =0,0
	for i,v in enumerate(lst):
		if v%2==0:
			en+=1
		else:
			on+=1
	return on - en

lst = [1, 2, 3]
print(up_and_down(lst))

lst = [1, 3, 5]
print(up_and_down(lst))

lst = [2, 4, 10, 2]
print(up_and_down(lst))