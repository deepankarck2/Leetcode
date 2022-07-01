# https://leetcode.com/problems/third-maximum-number/

class Solution:
     def thirdMax(self, nums):
        fm = sm = tm = None
        for num in nums:
            if(fm == None or num > fm):
                tm = sm
                sm=fm
                fm= num
            elif(fm == num):
                continue
            elif(sm==num):
                continue
            elif(sm == None or num > sm):
                tm=sm
                sm=num
            elif(tm==None or num>tm):
                tm = num

        if(tm is not None):
            return tm
        else:
            return fm
                

sol = Solution()

print(sol.thirdMax([5,2,2]))
