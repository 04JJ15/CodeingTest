'''
N개의 과목
우선순위 존재 과목마다
화살표가 들어오는 과목이 없다면 수료
모든 과목을 완료하는데 필요한 반복횟수, 불가능한 경우도 있음
'''

import sys
sys.stdin = open('sample_input2.txt')

test_case = int(input())

for tc in range(1, test_case+1):

    N = int(input())

    # x 번 과목의 선제과목 갯수, 그 과목의 번호
    mat = [list(map(int, input().split())) for _ in range(N)]

    graph = [0]*(N+1)
    graph[0] = []

    for i in range(1, N+1):
        if len(mat[i-1]) != 1:
            graph[i] = mat[i-1][1:]
        else:
            graph[i] = []

    collect = []
    cnt = 1
    while True:

        su = 0
        for i in range(len(graph)):
            su += len(graph[i])
        if su == 0:
            break

        empty_index = []
        for i in range(1, len(graph)):
            if len(graph[i]) == 0 and i not in collect:
                empty_index.append(i)
                collect.append(i)

        # 변화가 없으면 거기서 반복 종료
        if len(empty_index) == 0:
            cnt = -1
            break

        while empty_index:
            curr = empty_index.pop()
            for i in range(1, len(graph)):
                if curr in graph[i]:
                    graph[i].pop(graph[i].index(curr))

        cnt += 1

    print(f'#{tc} {cnt}')
