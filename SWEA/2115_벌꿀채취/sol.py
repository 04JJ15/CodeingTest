import sys
from itertools import combinations
sys.stdin = open('sample_input.txt')


def make_revenue(row, col, arr):  # C 이내로 얻을 수 있는 수익의 최대값을 [row, col, revenue]로 저장
    global C
    subset = []
    revenue = 0  # 수익

    for i in range(1, (1 << len(arr))):  # 비트마스킹
        for j in range(len(arr)):
            if (i & (1 << j)) != 0:
                subset.append(arr[j])
        if sum(subset) <= C:
            revenue = max(revenue, sum([num**2 for num in subset]))
        subset = []
    lis.append([row, col, revenue])


def select(array):  # 조합을 통해 모든 2쌍의 바구니 중 중복이 아니면서 최대 수익을 구해서 반환

    answer = 0
    select_list = combinations(array, 2)  # 조합
    for i in select_list:
        if i[0][0] != i[1][0]:
            answer = max(answer, i[0][2]+i[1][2])
        else:
            if i[0][1] + M <= i[1][1] or i[1][1] + M <= i[0][1]:
                answer = max(answer, i[0][2] + i[1][2])

    return answer


T = int(input())

for tc in range(1, T+1):

    N, M, C = map(int, input().split())
    bee = [list(map(int, input().split())) for _ in range(N)]

    lis = []  #

    for ro in range(N):
        for co in range(N-M+1):
            bee_bottles = bee[ro][co:co+M]  # 모든 바구니 경우의 수
            make_revenue(ro, co, bee_bottles)

    ans = select(lis)

    print(f'#{tc} {ans}')
