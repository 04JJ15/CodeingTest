import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    idx_list = [0]*(N+1)
    idx_list[1] = 1
    idx_list[2] = 3
    idx_list[3] = 6

    for i in range(4, N+1):
        idx_list[i] = idx_list[i-1] + 2*idx_list[i-2] + idx_list[i-3]

    print(f'#{tc} {idx_list[-1]}')
