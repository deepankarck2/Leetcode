def sol(nums):
    if nums:
        maxx = max(nums) + 1
        array = [None] * maxx

    for num in nums:
        array[num] = 1

    max_len = 0
    current_len = 0
    for i in range(len(array)):
        if (i+1 == len(array) or array[i+1] != None):
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
    return max_len


nums = [500, 100, 10, 21, 22, 55, 23, 56, 123, 56, 23, 24, 56, 234, 5542, 25]
print(sol(nums))
