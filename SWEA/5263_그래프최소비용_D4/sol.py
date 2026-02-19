import sys
sys.stdin = open('sample_input.txt')


def floyd_warshall(graph):
    dist = [[float('inf')] * N for _ in range(N)]

    for i in range(N):  # 자기 자신과의 거리는 0으로 초기화
        dist[i][i] = 0

    for u in range(N):
        for v in range(N):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    gra = [list(map(int, input().split())) for _ in range(N)]

    result = floyd_warshall(gra)
    ans = 0

    for i in result:
        ans = max(ans, max(i))

    print(f'#{tc} {ans}')
