def maxArea(height):
    max_area = 0
    start = 0
    end = len(height)-1

    while(start < end):
        x = end-start
        y = min(height[start], height[end])
        curr_area = x* y
        max_area = max( max_area, curr_area)
        if height[start] < height[end]:
            start+=1 
        else:
            end-=1
        
    return max_area

height = [1,8,6,2,5,4,8,3,7]
height = [1,1]

print(maxArea(height))