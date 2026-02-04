'''
다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.
- 8개의 숫자를 입력 받는다.
- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.
이와 같은 작업을 한 사이클이라 한다.
- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.
'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):

    N = int(input())

    lis = list(map(int, input().split()))

    cnt = 1  # 1~5를 반복할 카운트변수

    while True:  # 암호 규칙을 반복하면서 0이하의 숫자에 도달하면 종료
        lis.append(lis.pop(0) - cnt)
        if lis[-1] <= 0:
            lis[-1] = 0
            break
        cnt = cnt % 5 + 1

    print(f'#{N} {" ".join(map(str,lis))}')


