import sys
sys.stdin = open('sample_input.txt')

'''
1일 때가 시작지점
세로 N 가로 M 최대 50 * 50
시작위치 [R, M]
시간 L

'''
from collections import deque


def bfs(row, col, visited, move):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    lis = []
    queue = deque([(row, col)])
    visited[row][col] = True

    while move > 0:
        for _ in range(len(lis)):
            queue.append(lis.pop(0))
        while queue:
            ro, co = queue.popleft()
            up_ro, up_co = ro + dy[0], co + dx[0]
            down_ro, down_co = ro + dy[1], co + dx[1]
            left_ro, left_co = ro + dy[2], co + dx[2]
            right_ro, right_co = ro + dy[3], co + dx[3]


            if mat[ro][co] == 1 or mat[ro][co] == 2 or mat[ro][co] == 4 or mat[ro][co] == 7:  # 상
                if ro > 0:
                    if not visited[up_ro][up_co] and (mat[up_ro][up_co] == 1 or mat[up_ro][up_co] == 2 or mat[up_ro][up_co] == 5 or mat[up_ro][up_co] == 6):
                        lis.append((up_ro, up_co))
                        visited[up_ro][up_co] = True
            if mat[ro][co] == 1 or mat[ro][co] == 2 or mat[ro][co] == 5 or mat[ro][co] == 6:  # 하
                if ro < N-1:
                    if not visited[down_ro][down_co] and (mat[down_ro][down_co] == 1 or mat[down_ro][down_co] == 2 or mat[down_ro][down_co] == 4 or mat[down_ro][down_co] == 7):
                        lis.append((down_ro, down_co))
                        visited[down_ro][down_co] = True
            if mat[ro][co] == 1 or mat[ro][co] == 3 or mat[ro][co] == 6 or mat[ro][co] == 7:  # 좌
                if co > 0:
                    if not visited[left_ro][left_co] and (mat[left_ro][left_co] == 1 or mat[left_ro][left_co] == 3 or mat[left_ro][left_co] == 4 or mat[left_ro][left_co] == 5):
                        lis.append((left_ro, left_co))
                        visited[left_ro][left_co] = True
            if mat[ro][co] == 1 or mat[ro][co] == 3 or mat[ro][co] == 4 or mat[ro][co] == 5:  # 우
                if co < M-1:
                    if not visited[right_ro][right_co] and (mat[right_ro][right_co] == 1 or mat[right_ro][right_co] == 3 or mat[right_ro][right_co] == 6 or mat[right_ro][right_co] == 7):
                        lis.append((right_ro, right_co))
                        visited[right_ro][right_co] = True

        move -= 1


T = int(input())
for tc in range(1, T+1):

    N, M, R, C, L = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False]*M for _ in range(N)]

    bfs(R, C, visited, L-1)

    ans = 0

    for i in range(N):
        ans += visited[i].count(True)

    print(f'#{tc} {ans}')
