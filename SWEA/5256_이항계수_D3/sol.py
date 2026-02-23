import sys
sys.stdin = open('sample_input.txt')


def solve(p, q):
    B = [[0 for _ in range(p + 1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, p) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]

    return B[n][p]


T = int(input())

for tc in range(1, T+1):

    n, a, b = map(int, input().split())

    ans = solve(a, b)
    print(f'#{tc} {ans}')
    