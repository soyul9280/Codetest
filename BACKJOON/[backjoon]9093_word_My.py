import sys
T = int(input())
for i in range(T):
    words=sys.stdin.readline().split( )
    result=[]
    for word in words:
        result.append(word[::-1])
    sentence=" ".join(result)

