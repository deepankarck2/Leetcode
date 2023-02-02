def threeSum(nums):
    nums = sorted(nums)
    ans = []
    return ans

# TODO : Finish it with Python


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))


mydtct = {}
mydtct['f'] = 3

mydtct.setdefault('g', 5)
print(mydtct)
mydtct.update({'g': 100})
print(mydtct.get('g'))


myStack = [1, 2, 3]

print(myStack.pop(-1))
print(myStack)
