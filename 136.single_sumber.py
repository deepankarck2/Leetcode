#https://leetcode.com/problems/single-number/ 
 
def sol1(nums):
    #HashSet is prpbably a better approach
    # Continue adding ,and then remove if u see it twice 
     
        myDict = {}

        for num in nums:
            myDict.setdefault(num,0)
            myDict[num]+=1

        valSet = list(myDict.values())
        index = valSet.index(1)

        keySet = list(myDict.keys())
        return(keySet[index])


#Using BIT MANIPULATION 
#XOR 
# 0 XOR 0 = 0,    1 XOR 0 = 1
# https://www.youtube.com/watch?v=pb-o1WherYI 

def sol2(nums):
    answer = 0
    for num in nums:
        answer = num^answer

    return answer

"""
    Input: nums = [4,1,2,1,2]
    Output: 4
"""
nums = [4,1,2,1,2]

print(sol2(nums))

