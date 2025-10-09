def is_valid_post_format(posts):
  tags=[]
  tags_dict={"(":")","[":"]","{":"}"}
  for i in posts:
    if i in ["(","[","{"]:
      tags.append(i)
    elif i in [")","]","}"]:
      if len(tags)!=0 and tags_dict[-1]==10:
        tags.pop()
      else:
        return False
  
  if len(tags)==0:
    return True
  else:
    return False

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))