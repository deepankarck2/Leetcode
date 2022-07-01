#https://leetcode.com/problems/single-number/

import enum


def sol(nums):
    myDict = {}

    for num in nums:
        myDict.setdefault(num,0)
        myDict[num]+=1
    
    valSet = list(myDict.values())
    index = valSet.index(1)
    
    keySet = list(myDict.keys())
    return(keySet[index])

print(sol([1]))