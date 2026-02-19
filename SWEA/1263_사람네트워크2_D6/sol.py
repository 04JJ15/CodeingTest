import sys
sys.stdin = open('input.txt')


def floyd_warshall(graph):
    g_len = len(graph)
    dist = [[float('inf')]*g_len for _ in range(g_len)]

    for i in range(g_len):  # 자기자신은 0으로 채우기
        dist[i][i] = 0

    for u in range(g_len):  # 그래프의 인접행렬이 주어진 경우 채우기
        for v in range(g_len):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]

    for k in range(g_len):  # 정점을 거처가며 최소거리 구하기
        for i in range(g_len):
            for j in range(g_len):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


T = int(input())

for tc in range(1, T+1):

    mat = list(map(int, input().split()))

    N = mat[0]

    matrix = [[0]*N for _ in range(N)]  # 인접 행렬 만들기
    for i in range(N):
        for j in range(N):
            matrix[i][j] = mat[i*N+j+1]

    result = floyd_warshall(matrix)
    ans = 1000000000

    for i in result:
        ans = min(ans, sum(i))

    print(f'#{tc} {ans}')
