import sys
sys.stdin = open('input.txt')


def solve(st):
    bad_char = {}
    for i in range(len(st)):
        bad_char[st[i]] = i
    return bad_char


T = int(input())

for tc in range(1, T+1):

    A, B = input().split()
    ans = 0

    bad_char = solve(B)
    m = len(B)
    n = len(A)
    i = 0

    while i <= n - m:
        j = m - 1  # 시작

        while j >= 0 and B[j] == A[i+j]:
            j -= 1

        if j < 0:
            i += m
            ans += 1
        else:
            skip = j - bad_char.get(A[i+j], -1)
            i += max(1, skip)
            ans += max(1, skip)

    ans += (n - i)

    print(f'#{tc} {ans}')
