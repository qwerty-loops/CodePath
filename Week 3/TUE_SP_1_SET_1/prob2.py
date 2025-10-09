# # 1. Import the deque module
# from collections import deque 

# # 2. Initialize a new deque object (a new queue)
# queue = deque()

# #3. Add a new element, 1, to the end (right side) of the queue
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.appendleft(4)
# print(queue)

# print(queue.pop())
# print(queue.popleft())

# print(queue)

def reverse_comments_queue(comments):
  
    # return (comments[::-1])
    stack=[]
    comments_copy=comments.copy()
    for i in comments:
        stack.append(comments_copy.pop())
    return stack
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))