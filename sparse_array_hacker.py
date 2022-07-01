# https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&utm_campaign=email_campaign&utm_medium=email&utm_source=email 

import string
from unittest import result


def matchingStrings(strings, queries):
    string_dict={}
    for item in strings:
        string_dict.setdefault(item,0)
        string_dict[item]+=1 
    
    result =[]
    for item in queries:
        if item in string_dict:
            result.append(string_dict.get(item))
        else:
            result.append(0)

    return result


strings = []
queries = ["aba", "xzxb", "ab"]
print(matchingStrings(strings, queries))
