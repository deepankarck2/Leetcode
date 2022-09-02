#https://leetcode.com/problems/first-unique-character-in-a-string/

# Time: O(n)
# Space: O(1) --> there will be only 26 possible values in the dict.

from pprint import pprint
from turtle import width


def sol(s):
    dict = {}
    for char in s:
        dict.setdefault(char,0)
        dict[char]+= 1

    for char in dict.keys():
        if dict[char] == 1:
            return s.index(char)
    
    return -1

    
s = "aabb"

print(sol(s))