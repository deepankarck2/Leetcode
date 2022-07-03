#https://leetcode.com/problems/reverse-integer/

def sol(x):
    y = 0
    sin = False
    if x < 0:
        sin = True
        x = abs(x)

    while(abs(x) > 0):
        if(abs(y) > 2**31/10):
            return 0 
        y = (y*10) + (x % 10)
        x = x//10
        

    return y if not sin else -y

def sol2(x):
    pass 

x = 123

print(sol(x))


'''
JAVA

public int reverse(int x){
    boolean sign = x > 0; 
 
    x = Math.abs(x); 

    int resule = 0; 

    while(x > 0){
        if(result > Integer.MAX_VALUE/10) return 0; 
        result = (result * 10) + (x % 10); 
        x = x/10 ; 
    }

    return sign ? result: -result
}
'''