def exclusive_elemts(lst1, lst2):
	newlst=[]
	for i in lst1:
		if i not in lst2:
			newlst.append(i)
	for j in lst2:
		if j not in lst1:
			newlst.append(j)
	return newlst
		

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))

#Time complexity for above is O(n*m)
#Time complexity for loop 1 is O(n)
#Time complexity for loop 2 is O(m)

#Space Complexity for above is O(n+m)


#OR

#Using sets to make operation faster

def exclusive_elemts(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    newlst = []

    # Keep order by scanning lst1 first
    for x in lst1:
        if x not in set2:   # O(1) check
            newlst.append(x)

    # Then scan lst2
    for x in lst2:
        if x not in set1:   # O(1) check
            newlst.append(x)

    return newlst

#Time complexity for above is O(n+m)
#Space Complexity for above is O(n+m)
