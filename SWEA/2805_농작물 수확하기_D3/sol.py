'''
N X N크기의 농장이 있다.
① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.

[제약 사항]
농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)
농작물의 가치는 0~5이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

import sys
sys.stdin = open('input.txt')

# def mar(n):
#
#     if n == 0 or n == len(mat)-1:
#         return mat[n][len(mat) % 2]


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    mat = [list(map(int, input().strip())) for _ in range(N)]

    mid = N // 2
    ans = sum(mat[mid])

    for i in range(mid):
        ans = ans + sum(mat[i][mid-i:mid+i+1]) + sum(mat[N-1-i][mid-i:mid+i+1])

    print(f'#{tc} {ans}')