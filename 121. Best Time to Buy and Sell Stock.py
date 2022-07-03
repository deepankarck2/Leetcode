#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    maxProf = 0 
    buy = 0 

    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i+1, len(prices)):
            sell = prices[j]
            if(sell > buy):
                prof = sell-buy
                maxProf = max(maxProf, prof)
    return maxProf

def maxProfit2(prices):
    maxProf = 0 

    for i in range(len(prices)):
        buy = prices[i]
        sell = max(prices[i:len(prices)])
        if(sell > buy):
            prof = sell-buy
            maxProf = max(maxProf, prof)

    return maxProf

def maxProfit3(prices):
    maxProf = 0 
    buy = prices[0]
    
    for i in range(len(prices)):
        if(prices[i] <= buy):
            buy = prices[i]
        elif(prices[i] > buy):
            sell = prices[i]
            prof = sell - buy
            maxProf = max(maxProf,prof)

    return maxProf


prices =  [7,6,4,3,1]

print(maxProfit(prices))
print(maxProfit3(prices))