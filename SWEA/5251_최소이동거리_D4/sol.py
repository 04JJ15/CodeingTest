import sys
sys.stdin = open('sample_input.txt')

import heapq

T = int(input())

for tc in range(1, T+1):

    N, E = map(int, input().split())

    edges = {i: {} for i in range(N+1)}  # 그래프의 간선:점수 딕셔너리
    for i in range(E):
        s, e, w = map(int, input().split())
        edges[s][e] = w

    distance = [0] + [float('inf')] * N  # 정점마다 점수 저장

    edge_list = [[0, 0]]  # 현재 거리, 현재 정점을 저장하는 힙큐

    while edge_list:  # 다익스트라

        curr_dis, curr_node = heapq.heappop(edge_list)

        if distance[curr_node] < curr_dis:
            continue

        for node, score in edges[curr_node].items():
            dist = curr_dis + score
            if dist < distance[node]:
                distance[node] = dist
                heapq.heappush(edge_list, [dist, node])

    print(f'#{tc} {distance[-1]}')
