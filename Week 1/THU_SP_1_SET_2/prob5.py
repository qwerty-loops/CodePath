def move_zeroes(lst):
    new_lst=[]
    z_lst=[]
    i=0
    while i<len(lst):
        if lst[i]!=0:
            new_lst.append(lst[i])
            i+=1
        else:
            z_lst.append(lst[i])
            i+=1
    new_lst.extend(z_lst)
    return new_lst

lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))