def locate_thistles(items):
	found_thistle = []
	if len(items) == 0:
		return found_thistle
	else:
		for i in range(len(items)):
			if items[i] == "thistle":
				found_thistle.append(i)
		return found_thistle
				


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))


#Alternatively

def locate_thistles(items):
	found_thistle = []
	if len(items) == 0:
		return found_thistle
	else:
		for index,value in enumerate(items):
				if value == 'thistle':
					found_thistle.append(index)
		return found_thistle
				


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))

