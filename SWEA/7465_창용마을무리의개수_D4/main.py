import sys
sys.stdin = open('s_input.txt')

from collections import deque


# O((N+M)α(N))
def by_set():

    def make_set(k):
        parent = list(i for i in range(k+1))
        rank = [0] * (k+1)
        return parent, rank


    def find_set(x):
        if parent[x] != x:
            parent[x] = find_set(parent[x])
        return parent[x]


    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)

        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    parent, rank = make_set(N)

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    count = set()  # 집합을 통해 무리 중복 제거

    for i in range(1, N + 1):
        temp = find_set(i)
        count.add(temp)

    # 만약 모든 집합을 구해야 한다면?
    groups = {}
    for i in range(1, N + 1):
        root = find_set(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    return len(count), list(groups.values())


# O(N+M)
def by_dfs():
    graph = [[] for _ in range(N+1)]
    groups = []  # 모든 집합 담기

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N+1)

    def dfs(node, cur_group):
        visited[node] = True
        cur_group.append(node)
        for friend in graph[node]:
            if not visited[friend]:
                dfs(friend, cur_group)

    count = 0
    for i in range(1, N+1):
        if not visited[i]:
            new_group = []
            dfs(i, new_group)
            groups.append(new_group)
            count += 1

    return count, groups


# O(N+M)
def by_bfs():
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)

    def bfs(start):
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()

            for friend in graph[node]:
                if not visited[friend]:
                    visited[friend] = True
                    queue.append(friend)

    count = 0
    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
            count += 1

    return count

'''
집합의 개수를 구하기, 집합의 목록 구하기
union-find 방식은 메모리 제한이 심할 때, 간선의 개수가 정점에 비해 매우 많을 때 <- 거의 완전 그래프
간선이 추가될 때 마다 로직이 있는 문제를 풀때 유리하다.
union-find 방식은 집합의 수, 집합 내 원소의 수, 내부 원소의 연결성 확인 에서 사용하기 편하다
집합의 목록을 구해야 할 때는 한번 순회하면서 찾아보거나, 병행해서 관리해야함
dfs, bfs 는 간선이 제공된 상황에서 집합의 목록을 구하는 경우 후처리 없이 바로 구할 수 있음
대신 메모리를 많이 잡아먹는다. 
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{tc} {by_set()}')
    # print(f'#{tc} {by_dfs()}')
    # print(f'#{tc} {by_bfs()}')
