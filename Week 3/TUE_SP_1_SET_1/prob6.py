# def edit_post(post):
  
#   new_post = post.split(" ")
#   new_str=[]
#   for word in new_post:
#     new_str.append(word[::-1])
#   return " ".join(new_str)


from collections import deque

def edit_post(post):

    split_post=post.split(" ")
    queue=deque()
    for i in split_post:
        queue.append(i)
    return queue

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 