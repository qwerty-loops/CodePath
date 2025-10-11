# #Original Solution

# def engagement_boost(engagements):
#     #Creates an empty list
#     squared_engagements = []
    
#     #Iterating through list and squaring elememnts by multiplying it with itself
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         squared_engagements.append((squared_engagement, i)) #List of tuples appended
    
#     #Sorting in reverse order
#     squared_engagements.sort(reverse=True)
#     print(squared_engagements)
    
#     #Initializing another empty list based on size of engagaments
#     result = [0] * len(engagements)
#     position = len(engagements) - 1 #Length of engagaments list
    

#     #Iterating through tuple
#     #Assigning value to list position starting from end (greatest value)
#     #Reduce value of position and fill in for smaller values
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
    
#     #Return
#     return result


# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))



#OR

def engagement_boost(engagements):

    left,right=0,len(engagements) -1
    result = [0] * len(engagements)
    pos = len(engagements)-1

    while left <=right:

        ls=engagements[left] ** 2
        rs=engagements[right] ** 2

        if ls>rs:
            result[pos]=ls
            left+=1
        else:
            result[pos]=rs
            right-=1
        pos-=1

    return result

print(engagement_boost([-4, -1, 0, 9, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))