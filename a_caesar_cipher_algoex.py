def caesarCipherEncryptor(string, key):
    answer = ""

    for char in string:
        letter = ord(char) + (key % 26)

        if letter <= 122:
            pass
        else:
            letter = letter-122+96 
           
        answer += chr(letter)
    
    return answer 

def caesarCipherEncryptor2(string,key):
    answer = ""

    for char in string:
        letter = ord(char) + (key%26)

        if(letter <= 122):
            answer+= chr(letter)
        else:
            answer+= chr(96+letter % 122)

    return answer

string = "kjwmntauvjjnmsagwgawkagfuaugjhawgnawgjhawjgawbfawghesh"
print(caesarCipherEncryptor(string,55))
print(caesarCipherEncryptor2(string,55))