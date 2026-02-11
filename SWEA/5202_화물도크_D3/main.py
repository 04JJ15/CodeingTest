import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    timeline = [tuple(map(int, input().split())) for _ in range(N)]
    timeline.sort(key=lambda x: x[1])

    count = 0
    last_end = 0

    for start, end in timeline:
        if start >= last_end:  # 이전 일이 끝난 후 시작 가능하면
            count += 1
            last_end = end

    print(f'#{tc} {count}')
