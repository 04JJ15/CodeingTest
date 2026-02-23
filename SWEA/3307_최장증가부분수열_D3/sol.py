import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    lis = list(map(int, input().split()))

    # 뒤에서부터 역산하면서 a 인덱스에서 최대 길이를 저장한다

    idx_list = [0]*N  # k 인덱스에서의 최대 길이를 저장

    for i in range(len(lis)-2, -1, -1):
        for j in range(i+1, len(lis)):
            if lis[i] < lis[j]:
                idx_list[i] = max(idx_list[i], 1 + idx_list[j])  # 다음 스텝을 밟았을 때의 길이랑 비교

    print(f'#{tc} {max(idx_list)+1}')
