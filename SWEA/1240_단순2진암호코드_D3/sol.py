'''
1. 암호코드는 8개의 숫자로 이루어져 있다.

2. 암호코드에서의 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 암호코드의 가로 길이는 56이다.
   ※ 길이가 56가 아닌 코드는 주어지지 않는다. 주어진 암호코드는 주어진 규칙대로 해독할 수 있음을 보장한다.
      암호코드의 각 숫자가 암호화되는 규칙은 주어진 그림1을 참고하라.

3. 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.
    ex) 암호코드가 88012346일 경우,
    ( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 + 6) = 60은 10의 배수이므로 올바른 암호코드다.
    ex) 암호코드가 19960409일 경우,
    ( ( 1 + 9 + 0 + 0 ) x 3 ) + ( 9 + 6 + 4 + 9) = 58은 10의 배수가 아니므로 잘못된 암호코드다.
'''

import sys
sys.stdin = open('input.txt')

# 암호 딕셔너리로 하드코딩
dic = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001',
       6: '0101111', 7: '0111011', 8:'0110111', 9: '0001011'}

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    mat = [list(map(int, input().strip())) for _ in range(N)]

    # 2차원 리스트에서 1이 처음 존재하는 행을 찾고 그 행을 lis로 저장
    lis = []
    for i in range(N):
        if 1 in mat[i]:
            lis = mat[i]
            break

    # 암호 구조가 마지막은 모두1로 끝나므로 리스트를 뒤집어서 1의 위치를 찾고 거기서 -56으로 암호문을 특정해냄
    lis2 = list(reversed(lis))
    lis = lis[M-lis2.index(1)-56:M-lis2.index(1)]

    lis_ans = []

    # 암호문을 7개씩 나눠서 딕셔너리와 대조해서 십진수로 만들고 lis_ans에 저장
    for i in range(8):
        st = ''
        for j in range(7):
            st += str(lis[i*7+j])

        for key, value in dic.items():
            if value == st:
                lis_ans.append(key)
                break

    # 암호가 성립하는 조건과 출력코드
    su = sum(lis_ans[0::2])*3+sum(lis_ans[1::2])
    ans = 0

    if su % 10 != 0:
        ans = 0
    else:
        ans = sum(lis_ans)

    print(f'#{tc} {ans}')
