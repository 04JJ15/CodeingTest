import sys
sys.stdin = open('sin.txt')

# 최대 50개의 주머니
# 나눠준 사탕바구니의 max - min 이 최소가 되도록

T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())
    candy_pot = list(map(int, input().split()))

    ans = float('inf')
    candy_pot.sort()
    dif = []
    for i in range(N-1):
        dif.append(candy_pot[i+1] - candy_pot[i])

    for i in range(len(dif)-K+2):
        ans = min(ans, sum(dif[i:i+K-1]))

    print(f'#{tc} {ans}')
