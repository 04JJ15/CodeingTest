'''
[제약 사항]
자성체는 테이블 앞뒤 쪽에 있는 N극 또는 S극에만 반응하며 자성체끼리는 전혀 반응하지 않는다.
테이블의 크기는 100x100으로 주어진다. (예시에서는 설명을 위해 7x7로 주어졌음에 유의)

[입력]
10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 정사각형 테이블의 한 변의 길이가 주어진다. (이 값은 항상 100이다)
그 다음 줄부터 100 x 100크기의 테이블의 초기 모습이 주어진다.
1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미하며
테이블의 윗부분에 N극이 아래부분에 S극이 위치한다고 가정한다.
(N극 성질을 가지는 자성체는 S극에 이끌리는 성질이 있다.)

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 교착 상태의 개수를 출력한다.
'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):

    N = int(input())  # 100
    mat = [list(map(int, input().split())) for _ in range(N)]

    deadlock = 0  # 교착상태를 저장할 변수

    # 1은 아래로 2는 위로 N * N
    for i in range(N):
        temp = 0 # 위에서 아래로 진행하면서 1을 만나면 temp 에 저장
        idx = 0

        while idx != N:

            if temp == 1 and mat[idx][i] == 2: # 1이 저장된 상태로 2를 만나면 교착상태, temp 초기화
                deadlock += 1
                idx += 1
                temp = 0
            elif mat[idx][i] != 1:
                idx += 1
            else:
                temp = 1
                idx += 1

    print(f"#{tc} {deadlock}")
