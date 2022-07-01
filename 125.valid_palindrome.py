#https://leetcode.com/problems/valid-palindrome/ 


from traceback import print_tb


def sol2(s):
    modified = ''.join(e.lower() for e in s if e.isalnum())
    low  = 0
    high = len(modified)-1
   
    while(low < high):
        
        if(modified[low] != modified[high]):
            return False

        low+=1 
        high-=1

    return True



def sol(s):
    modified = ''.join(e.lower() for e in s if e.isalnum())
    high = len(modified)-1
    length = len(modified)
   
    for i in range(0, length//2):
        if(modified[i] != modified[high]):
            return False
        high-=1 

    return True

s= "A man, a plan, a canal: Panama"

print(sol2(s))