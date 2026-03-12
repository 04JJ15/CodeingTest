import sys
sys.stdin = open('input.txt')

# n개의 연속된 질문
# 정답을 맞추면 1점, 연속해서 맞추면 카운터 숫자 1증가, 틀리면 카운터가 초기화되서 0
# 카운터가 K가 되면 플레이어의 점수가 두 배가됨
MOD = 1000000009

T = int(input())

for tc in range(1, T+1):

    N, M, K = map(int, input().split())

    wrong = N - M  # 0의 개수
    can = min(M // (K-1), wrong)  # 0의 개수랑, M을 K-1번 반복할 수 있는 횟수 중 더 작은걸 구해

    wrong -= can
    M -= (K-1)*can
    N -= K*can
    score = (K-1)*can

    if wrong > 0:
        score += M
    else:
        # 남은 N 만큼이 모두 1로 채워진다는 뜻
        mod = N // K
        semi_score = pow(2, mod+1, MOD) - 2
        score += semi_score * K + (N % K)

    print(score % MOD)
