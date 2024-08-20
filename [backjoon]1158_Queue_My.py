n, k = map(int, input())
people = [for i in range(1, n+1)]
result = []
while people:
    for u in range(k-1):
        people.append(people.popleft())
    result.append()