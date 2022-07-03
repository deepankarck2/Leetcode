#https://www.algoexpert.io/questions/run-length-encoding

def sol(string):
    answer = []
    curr_count = 0 
    curr_char = string[0]

    for i in range(len(string)+1):
        
        if(i < len(string) and string[i] == curr_char):
            curr_count+= 1
        else:
            insert = 0 
            while(insert+9 < curr_count):
                answer.append(str(9))
                answer.append(curr_char)
                insert += 9
            answer.append(str(curr_count- insert))
            answer.append(curr_char)
            curr_count = 1
        curr_char = string[i] if i < len(string) else string[i-1]

    return "".join(answer)

def sol2(string):
    
    pass 

string = "AAAAAAAAAAAAABBCCCCDD"

print(sol(string))