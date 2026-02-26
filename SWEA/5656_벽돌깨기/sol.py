'''
N번의 구슬 타격, 구슬은 좌 우로만 움직임
구슬에 타격되면 벽돌의 숫자(1~9)만큼 상하좌우의 벽돌을 없앤다 1일경우 자기자신만
벽돌의 분쇄여파로 파괴된 벽돌도 하좌우의 벽돌을 없앤다.
과정이 종료된 후 벽돌은 아래로 떨어짐
w행 h열의 벽돌매트릭스가 주어짐
최대한 벽돌을 많이 부수기
N<=4 H<=15 W<=12
'''

import sys
sys.stdin = open('sample_input.txt')
import copy


def drop(wall):
    for col in range(W):
        # 해당 열에서 0이 아닌 벽돌만 추출
        bricks = [wall[row][col] for row in range(H) if wall[row][col] != 0]

        # 위쪽은 0으로, 아래쪽은 벽돌로 채우기
        empty = H - len(bricks)
        for row in range(H):
            if row < empty:
                wall[row][col] = 0
            else:
                wall[row][col] = bricks[row - empty]

    return wall

def boom(idx, value, wall):
    wall[idx[0]][idx[1]] = 0  # 먼저 0으로 만들고
    for val in range(1, value):
        for x, y in [(0, -val), (0, val), (-val, 0), (val, 0)]:
            new_y = idx[0] + y
            new_x = idx[1] + x
            if 0 <= new_x <= W-1 and 0 <= new_y <= H-1:
                next_val = wall[new_y][new_x]  # 값을 먼저 읽고
                if next_val == 0:
                    continue
                wall[new_y][new_x] = 0          # 0으로 만든 뒤
                if next_val > 1:
                    boom((new_y, new_x), next_val, wall)  # 그 다음 재귀
    return wall


def solve(matrix, cnt):

    if cnt == N:  # N회 구슬 타격했다면
        num = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    num += 1
        ans[0] = min(ans[0], num)  # 이전 값과 비교해서 저장
        return

    if sum(matrix[-1]) == 0:
        ans[0] = 0
        return

    for i in range(W):
        target_idx = ()
        target_value = 0
        for j in range(H):
            if matrix[j][i] != 0:
                target_idx = (j, i)  # y, x 좌표
                target_value = matrix[j][i]
                break

        if not target_idx:  # 해당 열에 벽돌 없으면 스킵
            continue

        # 연쇄폭발 로직(진행 후 남은 리스트를 반환)
        lis = copy.deepcopy(matrix)
        lis[target_idx[0]][target_idx[1]] = 0
        if target_value > 1:
            boom(target_idx, target_value, lis)
        drop(lis)
        solve(lis, cnt + 1)


T = int(input())

for tc in range(1, T+1):

    N, W, H = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(H)]

    ans = [0]
    ans[0] = 181

    solve(walls, 0)

    print(f'#{tc} {ans[0]}')