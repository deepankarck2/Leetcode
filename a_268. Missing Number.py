#https://leetcode.com/problems/missing-number/ 

from traceback import print_tb


def sol(nums):
    maxl = max(nums)
    minl = min(nums)

    myDict ={}
    
    for i in range(minl,maxl+1):
        if(i in nums):
            myDict.setdefault('1','')
            myDict['1']+= str(i)
        else:
            myDict.setdefault('0','')
            myDict['0']+= str(i)

    if('0' not in myDict):
        if(len(nums) in nums):
            return (minl-1)
        else:
            return maxl+1 

    return int(myDict['0'])
    

print(sol([1]))