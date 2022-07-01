#https://leetcode.com/problems/rotate-array/ 

#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]


#Works but uses extra space. Not what the problem wants. 
def sol1(nums,k):
    length = len(nums)
    k = k%length

    num2 = [None]*length
    
    for i in range(0,length):
        num2[(i+k)%length] = nums[i]
    
    nums[:] = list(num2)

def sol2(nums, k):
    pass

#$ TODO $: Do the O(1) space complexity solution 


nums = [-1,-100,3,99]
k = 2

sol1(nums,k)
print(nums)
