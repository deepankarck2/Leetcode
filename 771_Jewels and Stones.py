from traceback import print_tb
from numpy import char


def sol(jewels,stones):
    stone_count = {}
    jewels_count = 0 

    for chars in stones:
        stone_count.setdefault(chars, 0)
        stone_count[chars] += 1 
    
    for chars in jewels:
        if(chars in stone_count):
            jewels_count += stone_count[chars]

    return jewels_count

print(sol('z', 'ZZ'))
