import sys
sys.stdin = open('re_sample_input.txt')


def make_set(x):
    sett = [num for num in range(x+1)]
    ran = [0] * (x+1)
    return sett, ran


def find_set(x):
    if sets[x] != x:
        sets[x] = find_set(sets[x])
    return sets[x]


def union(a, b):
    root_a = find_set(a)
    root_b = find_set(b)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            sets[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            sets[root_a] = root_b
        else:
            sets[root_b] = root_a
            rank[root_a] += 1


tc = int(input())

for test in range(1, tc+1):

    N = int(input())
    N_x = list(map(int, input().split()))
    N_y = list(map(int, input().split()))
    E = float(input())

    # 간선리스트 만들기 n(n-1)/2
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            edges.append([i, j, (N_x[i] - N_x[j])**2 + (N_y[i] - N_y[j])**2])

    edges.sort(key=lambda x: x[2])

    sets, rank = make_set(N)
    count = 0  # 간선 수 세기
    cost = 0  # 가중치 더하기

    for i in range(len(edges)):
        if find_set(edges[i][0]) != find_set(edges[i][1]):
            cost += E * edges[i][2]
            union(edges[i][0], edges[i][1])
            count += 1
        else:
            continue
        if count == N-1:
            break

    print(f'#{test} {round(cost)}')
