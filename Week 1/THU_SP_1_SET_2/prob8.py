def left_right_difference(nums):
    answer=[]
    if len(nums)<=1:
        return [0]
    else:
        for i,v in enumerate(nums):
            if i==0:
                ls,rs=0,0
                rs+=sum(nums[i+1:])
                answer.append(ls-rs)
            elif i==(len(nums)-1):
                ls,rs=0,0
                ls+=sum(nums[:i])
                answer.append(ls-rs)
            else:
                ls,rs=0,0
                ls+=sum(nums[:i])
                rs+=sum(nums[i+1:])
                answer.append(ls-rs)
        return answer

nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))
