import sys
sys.stdin = open('input.txt')

# depth 만큼 time 증가
# 좌상단(S) -> 좌하단(G) 까지의 최소 복구 시간
import heapq

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().strip())) for _ in range(N)]
    lis = [[100000]*N for _ in range(N)]  # 좌표까지 도달하는 최소 비용을 저장할 리스트

    lis[0][0] = mat[0][0]

    heap = [(mat[0][0], 0, 0)]

    while heap:
        curr_cost, r, c = heapq.heappop(heap)

        if curr_cost > lis[r][c]:
            continue

        if r == N-1 and c == N-1:  # 목적지 도달
            print(f'#{tc} {lis[r][c]}')
            break

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r = r + dy
            new_c = c + dx
            if 0 <= new_r < N and 0 <= new_c < N:
                new_cost = curr_cost + mat[new_r][new_c]

                if new_cost < lis[new_r][new_c]:
                    lis[new_r][new_c] = new_cost
                    heapq.heappush(heap, (new_cost, new_r, new_c))
