#https://leetcode.com/problems/reverse-string/

def sol(s):
    high = len(s)-1
    str_length = len(s)

    for i in range(0,str_length//2):
        temp = s[high]
        s[high]=s[i]
        s[i]=temp
        high-=1



s = ["h","e","l","l","o"]

sol(s)
print(s)