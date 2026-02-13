import sys
sys.stdin = open('sample_input.txt')

import heapq

T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]

    for _ in range(E):  # 노드 별 간선을 미리 만들기
        a, b, c = map(int, input().split())

        node[a].append((b, c))
        node[b].append((a, c))

    ans = 0
    node_visit = [False]*(V+1)  # 노드 방문 처리
    edge_list = [(0, 1)]  # 간선을 담을 힙, 1번 정점부터 시작
    cnt = 0  # 방문한 노드 수

    while edge_list:  # 간선이 남았거나
        if cnt == V:  # 모든 정점을 방문 할 때까지 반복
            break

        score, curr = heapq.heappop(edge_list)  # 가장 가중치가 작은 간선을 선택하고

        if node_visit[curr]:
            continue

        node_visit[curr] = True  # 방문한적 없는 정점이면
        ans += score  # 방문한 것으로 표시
        cnt += 1

        for next_node, next_score in node[curr]:  # 그 정점에서 방문 가능한 간선들을 모두 삽입
            if not node_visit[next_node]:
                heapq.heappush(edge_list, (next_score, next_node))

    print(f'#{tc} {ans}')
