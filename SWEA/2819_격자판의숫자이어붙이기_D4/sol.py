import sys
sys.stdin = open('sample_input.txt')


def dfs(row, col, st):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    st += str(mat[col][row])

    if len(st) == 7:
        res.add(st)
        return

    for seed in range(4):
        nr = row + dx[seed]
        nc = col + dy[seed]

        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, st)


T = int(input())

for tc in range(1, T+1):

    mat = [list(map(int, input().split())) for _ in range(4)]

    res = set()  # 집합에 숫자모음 저장

    for i in range(4):
        for j in range(4):
            dfs(i, j, "")  # 모든 시작위치에서 dfs 진행

    print(f'#{tc} {len(res)}')
