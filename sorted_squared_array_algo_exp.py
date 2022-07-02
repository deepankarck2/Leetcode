#https://www.algoexpert.io/questions/sorted-squared-arrayy 


#make sure to care for the negative values. 
def sortedSquaredarrayy(arrayy):
    ret_list = [num**2 for num in arrayy]
    
    return sorted(ret_list)

#Efficient Solution using two pointer method 
def sol2(arrayy):
    low = 0 
    high = len(arrayy)-1
    ans_index = len(arrayy)-1

    answer = [None]*len(arrayy)

    while(low <= high):
        low_num = arrayy[low]
        high_num = arrayy[high]

        if(abs(low_num) > abs(high_num)):
            answer[ans_index] = low_num**2 
            ans_index-=1 
            low+=1 

        elif(abs(low_num) <= abs(high_num)):
            answer[ans_index] = high_num**2
            ans_index-=1
            high-=1

    return answer

    
arrayy = [-3,-2,-1]
print(sortedSquaredarrayy(arrayy))

print(sol2(arrayy))