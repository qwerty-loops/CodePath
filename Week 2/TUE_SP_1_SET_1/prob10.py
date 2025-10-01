def num_VIP_guests(vip_passes, guests):
    n=0
    for i in guests:
        if i in vip_passes:
            n+=vip_passes.count(i)
    return n

#OR

    c=0
    for i in guests:
        if i in vip_passes:
            c+=1
    return c

#OR

    c=0
    set1=set(vip_passes)
    for i in guests:
        if i in set1:
            c+=1
    return c

#OR
    vp={}
    for i in guests:
        if i not in vp:
            vp[i]=1
        else:
            vp[i]+=1

    s=0
    for i in vip_passes:
        if i in vp.keys():
            s+=vp[i]
    return s

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))