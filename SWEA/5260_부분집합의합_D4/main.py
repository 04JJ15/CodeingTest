import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())

    dp = [0] * (K + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(K, i - 1, -1):
            dp[j] += dp[j - i]

    print(f'#{tc} {dp[-1]}')