import sys
input= sys.stdin.readline()
n,m=map(int,input().split())
answer=[]
def sol():
    if len(answer)==m:
        print(answer)
        return
    