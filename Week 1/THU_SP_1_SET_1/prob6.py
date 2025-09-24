def is_acronym(words, s):
    c=0
    for i,v in enumerate(words):
        if v[0] == s[i]:
            c+=1
    if c==3:
        return True
    else:
        return False
            

words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

words = ["Pooh","Bear"]
s = "bp"
print(is_acronym(words, s))