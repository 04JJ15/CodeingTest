import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(row, col):
    queue = deque([(row, col)])

    while queue:
        ro, co = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_r = ro + dy
            next_c = co + dx
            if mat[next_r][next_c] == 3:
                return 1
            elif mat[next_r][next_c] == 0:
                queue.append((next_r, next_c))
                mat[next_r][next_c] = 1

    return 0


for tc in range(1, 11):

    N = int(input())
    mat = [list(map(int, input().strip())) for _ in range(100)]
    c, r = 0, 0
    ans = 0

    for i in range(100):
        if 2 in mat[i]:
            c = mat[i].index(2)
            r = i
            break

    ans = bfs(r, c)
    print(f'#{tc} {ans}')
