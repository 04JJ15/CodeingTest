'''
N개의 컨테이너를 M개의 트럭으로  A->B 도시로 N,M은 최대 100개
트럭당 1개의 컨테이너 용량초과한 컨테이너는 운반 불가
한번만 이동함, 중량을 최대로 했을 때 전체 무게, 한개로 못옮기면 0
'''
import sys
sys.stdin = open('sample_input.txt')


def solve(truc, index):
    global ans

    for con in range(index, len(con_weight)):
        if truc >= con_weight[con]:
            ans += con_weight[con]
            idx[0] = con+1
            break


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    con_weight = list(map(int, input().split()))
    truck_weight = list(map(int, input().split()))
    ans = 0
    idx = [0]

    con_weight.sort(reverse=True)
    truck_weight.sort(reverse=True)

    for truck in truck_weight:
        solve(truck, idx[0])
        if idx[0] == len(con_weight):
            break

    print(f'{tc} {ans}')
