'''
[Fig. 1] 과 같은 N * N 크기의 절벽지대에 활주로를 건설하려고 한다.
각 셀의 숫자는 그 지형의 높이를 의미한다.

활주로는 높이가 동일한 구간에서 건설이 가능하다. 가로랑 세로

높이가 다른 구간의 경우 활주로가 끊어지기 때문에 [Fig. 3] 과 같은 경사로를 설치해야만 활주로를 건설 할 수 있다.
경사로는 길이가 X 이고, 높이는 1 이다.
경사로는 높이 차이가 1 이고 낮은 지형의 높이가 동일하게 경사로의 길이만큼 연속되는 곳에 설치 할 수 있다.

경사로의 길이 X 와 절벽지대의 높이 정보가 주어질 때,
활주로를 건설할 수 있는 경우의 수를 계산하는 프로그램을 작성하라.
'''

import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, X = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 행 과 열로 나누어서 만족하는 값을 찾는다 구조는 동일
    for i in range(N):

        temp = 0
        before = 0
        same_cnt = 0
        idx = 0
        while idx != N: # (0,0)에서 오른쪽으로 진행하면서 만족하지 않은 값이 있으면 반복문을 종료하고 문제없이 반복문의 종료코드에 도달하면 ans에 1을 추가한다
            before = temp
            temp = mat[i][idx]
            if before == 0 or before == temp: # 현재 좌표의 값을 temp에 이전 값을 before에 저장, 둘의 값을 비교해서 같으면 same_cnt에 누적시킨다
                same_cnt += 1
                idx += 1
            else: # 값이 다른 상황이 생기면 차가 1 or -1이냐에 따라 분기를 나눔
                if before - temp == -1 and same_cnt >= X: # -1 일 경우 ex) 2223 same_cnt가 X보다 크거나 같으면 그대로 진행한다
                    same_cnt = 1
                    idx += 1
                elif before - temp == 1: # 1 일 경우 ex) 33222 temp에서 X만큼의 여유거리가 남았는지 확인하고
                    if len(mat[i][idx:]) < X:
                        break
                    else:
                        if mat[i][idx:idx + X].count(temp) == X: # X만큼의 거리가 모두 같은 숫자로 이뤄져 있는지 검증한다
                            same_cnt = 0
                            idx += X
                        else:
                            break
                else:
                    break
        if idx == N:
            ans += 1

    for i in range(N):

        lis = []
        temp = 0
        before = 0
        same_cnt = 0
        idx = 0
        while idx != N:
            before = temp
            temp = mat[idx][i]
            if before == 0 or before == temp:
                same_cnt += 1
                idx += 1
            else:
                if before - temp == -1 and same_cnt >= X:
                    same_cnt = 1
                    idx += 1
                elif before - temp == 1:
                    if N - idx < X:
                        break
                    else:
                        su = 0
                        for j in range(X):
                            su += mat[idx + j][i]
                        if su == temp*X:
                            same_cnt = 0
                            idx += X
                        else:
                            break
                else:
                    break
        if idx == N:
            ans += 1

    print(f"#{tc} {ans}")

