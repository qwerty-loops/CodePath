def clean_post(post):
    post=post.lower()
    new_str=[]
    if post=="":
        return ""
    else: 
        for ch in post:
            if ch not in new_str:
                new_str.append(ch)
            elif ch.lower() in new_str:
                new_str.remove(ch)
        return "".join(new_str)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 