import sys
sys.stdin = open('sample_input.txt')


def make_set(k):
    parent = [i for i in range(k+1)]
    rank = [0] * (k+1)
    return parent, rank


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


tc = int(input())

for test in range(1, tc+1):

    N, M = map(int, input().split())
    lis = list(map(int, input().split()))

    parent, rank = make_set(N)
    count = set()  # 집합으로 무리의 중복을 제거한다

    for i in range(0, len(lis), 2):
        union(lis[i], lis[i+1])

    for i in range(1, N+1):
        temp = find_set(i)
        count.add(temp)

    print(f'#{test} {len(count)}')
