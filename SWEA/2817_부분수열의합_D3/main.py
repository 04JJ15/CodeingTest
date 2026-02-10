import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())  # N 최대 20 K 최대 100

    lis = list(map(int, input().split()))  # 1~100 이하의 정수
    ans = 0

    for i in range(1 << len(lis)):  # 비트마스킹
        subset_sum = 0
        for j in range(len(lis)):
            if (1 << j) & i:
                subset_sum += lis[j]
                if subset_sum > K:
                    break
        if subset_sum == K:
            ans += 1

    print(f'#{tc} {ans}')
