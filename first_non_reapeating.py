#https://www.algoexpert.io/questions/first-non-repeating-character 

def firstNonRepeatingCharacter(string):
    dict = {} 

    for char in string:
        dict.setdefault(char, 0)
        dict[char]+= 1
    
    for char in string:
        if dict[char] == 1:
            return string.index(char)
    return -1

string = "abcdcaf"
print(firstNonRepeatingCharacter(string))