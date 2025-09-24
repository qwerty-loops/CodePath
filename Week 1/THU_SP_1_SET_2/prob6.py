def reverse_vowels(s):
    s=s.lower()
    sl=list(s)
    f=0
    l=len(sl)-1

    while f<=l:
        if sl[f] in 'aeiou' and sl[l] in 'aeiou':
            temp = sl[f]
            sl[f] = sl[l]
            sl[l] = temp
            f+=1
            l-=1
        elif sl[f] in 'aeiou' and sl[l] not in 'aeiou':
            l-=1
        elif sl[f] not in 'aeiou' and sl[l] in 'aeiou':
            f+=1
        else:
            f+=1
            l-=1
    return "".join(sl)



s = "robin"
print(reverse_vowels(s))

s = "BATgirl"
print(reverse_vowels(s))

s = "batman"
print(reverse_vowels(s))