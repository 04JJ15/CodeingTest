import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    A = input()
    B = input()
    ans = 0

    dic = {}
    for i in range(len(A)):
        dic[A[i]] = i

    for i in dic.keys():
        cnt = 0
        for j in B:
            if i == j:
                cnt += 1

        ans = max(ans, cnt)

    print(f'#{tc} {ans}')
