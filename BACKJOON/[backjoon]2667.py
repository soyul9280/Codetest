from collections import deque

def bfs(graph, i, j):
    N = len(graph)
    need_visited = deque([])
    need_visited.append((i, j))

    graph[i][j] = '0'
    num_apt = 1

    # 상하좌우 탐색
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while need_visited:
        x, y = need_visited.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == '1':
                need_visited.append((nx, ny))
                graph[nx][ny] = '0'
                num_apt += 1

    return num_apt


N = int(input())
graph = []
for i in range(N):
    nodes = list(input())
    graph.append(nodes)

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)