from pprint import pprint
from turtle import width



def tournamentWinner(competitions, results):

    dict = {}
    arr_row = 0 

    for i in range(len(results)):
        if(results[i] == 0):
            team = competitions[arr_row][1] 
            dict[team] = dict.get(team,0) + 3              
        else:
            team = competitions[arr_row][0] 
            dict[team] = dict.get(team,0) + 3    
        
        arr_row+=1           
    
    maxx = max(dict, key = dict.get)
    return maxx

competitions  = [["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
    ]

results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]

print(tournamentWinner(competitions, results))