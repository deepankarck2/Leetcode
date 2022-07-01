#https://leetcode.com/problems/implement-strstr/ 

import enum
from operator import ne
from traceback import print_tb

from psutil import net_if_addrs


def sol(haystack,needle):
    if(not needle or not haystack):
        return 0
    
    for i in range(0, len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i: i+len(needle)] == needle:
                return i
    
    return -1

print(sol("mississippi", "issip"))
