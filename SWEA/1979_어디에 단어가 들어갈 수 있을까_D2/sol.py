'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

[제약 사항]
1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    cnt = 0
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N-K+1):
            if sum(mat[i][j:j+K]) == K:
                if j == 0:
                    if mat[i][j+K] == 0:
                        cnt += 1
                elif j == N-K:
                    if mat[i][j-1] == 0:
                        cnt += 1
                else:
                    if mat[i][j+K] == 0 and mat[i][j-1] == 0:
                        cnt += 1

    for i in range(N-K+1):
        for j in range(N):
            su = 0
            if i == 0 and mat[i+K][j] == 0:
                for p in range(i, i+K):
                    su += mat[p][j]
                if su == K:
                    cnt += 1

            elif i == N-K and mat[i-1][j] == 0:
                for p in range(i, i+K):
                    su += mat[p][j]
                if su == K:
                    cnt += 1

            elif mat[i-1][j] == 0 and mat[i+K][j] == 0:
                for p in range(i, i+K):
                    su += mat[p][j]
                if su == K:
                    cnt += 1

    print(f'#{tc} {cnt}')