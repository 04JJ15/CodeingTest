import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    # 물건 x의 가격 info[x]
    info = [list(map(int, input().split())) for _ in range(M)]
    lis = [0] * (N+1)

    for size, price in info:

        for j in range(N, size-1, -1):
            lis[j] = max(lis[j], lis[j - size] + price)

    print(f'#{tc} {lis[-1]}')