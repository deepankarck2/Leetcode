from re import L

#Pointer Approach 
def isPalindrome(string):
    high = len(string)-1 

    for i in range(0, len(string)//2):
        if(string[i] != string[high]):
            return False
        high-= 1 

    return True

#Recursion Approach 
def isPalindromeRecur(string):
    #Tail recursion... 

    length = len(string)
    
    if(length <= 1):
        return True
    if(string[0] != string[length-1]):
        return False
    else:
        return isPalindromeRecur(string[1:-1]) #Again extra calculation in the substring level
   
    #Or simply(Not tail recursion): 
    return string[0] == string[length-1] and isPalindromeRecur(string[1:-1])

def isPalindromeRecus_better(string, i =0):
    j = len(string)-1-i

    return True if i>=j else string[i]==string[j] and isPalindromeRecus_better(string,i+1)


text= "abbsa"  
print("Pointer Approach: ", isPalindrome(text))

print("Recursion: ", isPalindromeRecur(text))
print("Recursion: ", isPalindromeRecus_better(text))