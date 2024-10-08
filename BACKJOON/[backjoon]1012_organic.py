import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 정의
def dfs(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 있고 1이면(=배추이면) 지나간것을 -1로 표시하고 주변 탐색
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)

t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    graph = [[0 for _ in range(m)] for _ in range(n)]

    # 배추 위치 표시
    for _ in range(k):
        X, Y = map(int, input().split()) 
        graph[Y][X] = 1 # X, Y 바꿔서 표시해야하는거 주의!

    # 배추 그룹 수(=배추흰지렁이 개수) 세기
    count = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a ,b)
                count += 1
    print(count)