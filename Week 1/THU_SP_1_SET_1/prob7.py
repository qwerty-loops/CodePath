def make_divisible_by_3(nums):
    c=0
    for i,v in enumerate(nums):
        if v%3==0:
            pass
        else:
            c+=1
    return c


nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))