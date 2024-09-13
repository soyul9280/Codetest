import sys

N, S, M = map(int, sys.stdin.readline().strip().split())
d = {S}

V_list = list(map(int, sys.stdin.readline().strip().split()))

for V in V_list:
    temp = set()
    for volume in d:
        if volume + V <= M:
            temp.add(volume + V)
        if volume - V >= 0:
            temp.add(volume - V)
    d = temp

if not d:
    print(-1)
else:
    print(max(d))