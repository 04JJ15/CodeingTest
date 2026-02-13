import sys
sys.stdin = open('sample_input.txt')

import heapq


def prim(start):

    edges = [[] for _ in range(V+1)]  # 인접 리스트 만들기
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges[n1].append((w, n2))
        edges[n2].append((w, n1))

    edge_list = [(0, 0)]
    cnt = 0
    ans = 0  # 가중치를 더해줄 변수
    visited = [False] * (V+1)

    while edge_list:  # 간선이 남았다면,

        if cnt == V+1:  # 모든 노드를 추가했다면 반복 종료
            break

        cost, node = heapq.heappop(edge_list)  # 가장 가중치가 적은 간선을 선택

        if visited[node]:  # 방문 했던 정점이면 패스
            continue

        cnt += 1  # 노드 방문
        visited[node] = True  # 노드 방문
        ans += cost  # 가중치 합산

        for edge in edges[node]:  # 방문가능한 간선들을 모두 힙큐에 삽입
            heapq.heappush(edge_list, (edge[0], edge[1]))

    return ans


def make_set(n):

    p = list(range(n+1))
    rank = [0] * (n+1)
    return p, rank


def find_set(p, x):
    if p[x] != x:
        p[x] = find_set(p, p[x])
    return p[x]


def union(p, rank, a, b):
    root_a = find_set(p, a)
    root_b = find_set(p, b)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            p[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            p[root_a] = root_b
        else:
            p[root_b] = root_a
            rank[root_a] += 1


def kruskal():
    p, rank = make_set(V)
    ans = 0
    edges = 0

    edge_list = [list(map(int, input().split())) for _ in range(E)]
    edge_list.sort(key=lambda x: x[2])  # 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬

    for edge in edge_list:  # 가중치가 낮은 간선부터 선택
        if find_set(p, edge[0]) != find_set(p, edge[1]):  # 두 대표자가 다르다면,
            union(p, rank, edge[0], edge[1])
            ans += edge[2]  # 엣지를 최소 비용 집합에 추가
            edges += 1  # 간선이 선택된 횟수
        else:  # 두 대표자가 같다면 사이클이 생성되므로 무시
            continue

        if edges == V:  # n-1개의 간선이 선택될 때까지 반복
            break

    return ans


'''
크루스칼: O(ElogE) : 간선리스트 O(E) 완전그래프에 가까울 수록 정렬 비용 vs 우선순위 큐 비용의 문제가 됨 
프림: O(ElogV) : 인접리스트 O(V+E) 이미 일정 부분 조립된 그래프가 주어졌을 때 MST를 만들 때 좋음
'''
T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())  # V <= 1000, E <= 1000000

    result1 = prim(0)
    # result2 = kruskal()
    print(f'#{tc} {result1}')
