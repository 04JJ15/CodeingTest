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


T = int(input())

for tc in range(1, T+1):

    n, m = map(int, input().split())  # 1 <= n <= 1000000 1 <= m <= 100000

    ans = ""
    parent, rank = make_set(n)

    for i in range(m):
        num, a, b = map(int, input().split())
        if num == 0:
            union(a, b)
        else:
            if find_set(a) == find_set(b):
                ans += '1'
            else:
                ans += '0'

    print(f'#{tc} {ans}')
