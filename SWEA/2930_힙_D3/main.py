import sys
sys.stdin = open('sample_input.txt')

# 그냥 힙큐 썼습니다 ㅎ

import heapq

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    heap = []
    ans = []

    for i in mat:
        if i[0] == 1:
            heapq.heappush(heap, -i[1])
        else:
            if len(heap) == 0:
                ans.append(-1)
            else:
                ans.append(-heapq.heappop(heap))

    print(f'#{tc}', end=" ")
    print(*ans)
