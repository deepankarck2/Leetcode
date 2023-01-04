def threeSum(nums):
    nums = sorted(nums)
    ans = []
    for num in nums:
        new_sum = 0 - num
        a, b = two_sum(new_sum)


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
