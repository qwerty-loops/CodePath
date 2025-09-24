def goldilocks_approved(nums):
    num_min = min(nums)
    num_max = max(nums)
    nums.sort()
    if len(nums) <=2:
        return -1
    else:
        return nums[1]


nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))