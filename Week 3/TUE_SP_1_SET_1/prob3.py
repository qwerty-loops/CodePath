def is_symmetrical_title(title):

#   title=title.lower().replace(" ","")
#   if title==title[::-1]:
#     return True
#   else:
#     return False
    title=title.lower().replace(" ","")
    first,last=0,len(title)-1
    while first<last:
        if title[first]!= title[last]:
            return False
        else:
            first+=1
            last-=1
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 