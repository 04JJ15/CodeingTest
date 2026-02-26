import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())
    num_list = deque(map(str, input().strip()))

    rotate = len(num_list) // 4
    num_set = set()

    for i in range(rotate):  # 변의 길이만큼 회전
        for j in range(4):
            num_set.add(''.join(list(num_list)[j*rotate:j*rotate+rotate]))

        num_list.rotate(1)

    ans_list = []
    for i in num_set:
        ans_list.append(int(i, 16))
    ans_list.sort(reverse=True)

    print(f'#{tc} {ans_list[K-1]}')
