import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)
    ans_list = []

    for i in range(min(10, len(num_list))):
        if i % 2 == 0:
            ans_list.append(num_list[i//2])
        else:
            ans_list.append(num_list[i//2 - i])

    print(f"#{tc}", end=" ")
    print(*ans_list)
