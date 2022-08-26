# https://codeforces.com/problemset/problem/158/A

n, k = input().split() #how to take multiple input 
     
list1 = list(map(int, input().split()))  #Multiple input as a list
     
counter = 0 
beat = list1[int(k)-1]
     
for i in range(int(n)):
    if(list1[i] > 0 and list1[i] >= beat):
        counter+= 1
     
print(counter)