def canConstruct(ransomNote,magazine):
    magazineHash = {}

    for char in magazine:
        magazineHash.setdefault(char,0)
        magazineHash[char]+= 1
    
    for char in ransomNote:
        if(magazineHash.get(char,0) <= 0):
            return False
        else:
            magazineHash[char]-= 1
    
    return True

print(canConstruct("", "aab")) 
