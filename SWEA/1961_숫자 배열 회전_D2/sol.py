'''
N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


[제약 사항]

N은 3 이상 7 이하이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N이 주어지고,

다음 N 줄에는 N x N 행렬이 주어진다.

[출력]

출력의 첫 줄은 '#t'로 시작하고,

다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.

입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}')

    # 90도
    lis1 = []
    for i in range(N):
        st1 = ""
        for j in range(N-1, -1, -1):
            st1 += str(mat[j][i])
        lis1.append(st1)

    # 180도
    lis2 = []
    for i in range(N-1, -1, -1):
        st2 = ""
        for j in range(N-1, -1, -1):
            st2 += str(mat[i][j])
        lis2.append(st2)

    # 270도
    lis3 = []
    for i in range(N-1, -1, -1):
        st3 = ""
        for j in range(N):
            st3 += str(mat[j][i])
        lis3.append(st3)

    # 합치기

    for i in range(N):
        print(lis1[i], end=" ")
        print(lis2[i], end=" ")
        print(lis3[i])


