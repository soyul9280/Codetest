n,m = map(int, input().split())
s=[]
def dfs():
    if len(s)==m:
        print(' '.join())
    for i in range(1, n+1):
        s.append(i)