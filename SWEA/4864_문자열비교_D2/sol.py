import sys
sys.stdin = open('input.txt')


def solve(st):
    bad_char = {}
    for i in range(len(st)):
        bad_char[st[i]] = i
    return bad_char


T = int(input())

for tc in range(1, T+1):

    A = input()
    B = input()
    ans = 0

    bad_char = solve(A)
    m = len(A)
    n = len(B)
    i = 0

    while i <= n - m:
        j = m - 1  # 시작

        while j >= 0 and A[j] == B[i+j]:
            j -= 1

        if j < 0:
            ans = 1
            break
        else:
            skip = j - bad_char.get(B[i+j], -1)
            i += max(1, skip)

    print(f'#{tc} {ans}')
