def sol2(s):
    len_last = 0
    len_current = 0

    for char in s:
        if(char == ' '):
            len_current = 0
        else:
            len_current +=1 
            len_last = len_current
            
    return len_last

def sol(s):

    split_string = s.strip().split(" ")
    len_last = 0

    print(split_string)
    for char in split_string[len(split_string)-1]:
        len_last+= 1
    
    return len_last

print(sol2("   fly me   to   the moon  "))