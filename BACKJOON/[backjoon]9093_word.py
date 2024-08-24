import sys
T = int(input())
for i in range(T):
    words=sys.stdin.readline().split( )
    for word in words:
        print(word[::-1], end=' ')