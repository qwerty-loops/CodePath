def tiggerfy(s):
	s = s.strip().lower()
	new_s =""
	for i in s:
		if i != "t" and i !=  "i" and i !=  "g" and i !=  "e" and i != "r":
			new_s += i
	return new_s

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))