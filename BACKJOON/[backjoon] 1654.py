K, N = map(int, input().split()) 
lis = []   
for _ in range(K):
    lis.append(int(input()))  

s = 1   
e = max(lis)   

while s <= e:   
    mid = (s+e)//2   
    LAN = 0  
    for i in lis:
        LAN += i//mid  
    if LAN >= N:   
        s = mid + 1  
    else:   
        e = mid - 1  

print(e)