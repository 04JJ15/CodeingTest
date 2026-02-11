'''
도시의 크기 N <= 20 비용 M <= 10
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]

    house = []  # 집의 위치좌표를 모두 담음
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                house.append([i, j])
##################################################################################
    # K = 0
    # for i in range(21, 0, -1):  # 방범 사이즈가 최대 몇까지 가능한지
    #     if 1 + 2*(i**2 - i) <= len(house)*M:
    #         K = i
    #         break    <- 최대 수익을 통해 K의 max 값을 제한할 수 있을까 해봤는데 실패함
##################################################################################
    ans = 0
    for center_row in range(N):  # 모든 점을 순회
        for center_col in range(N):
            dist = []  # 그 점에서 모든 집까지의 거리를 리스트에 저장함
            for house_r, house_c in house:
                dist.append(abs(center_row - house_r) + abs(center_col - house_c))

            dist.sort()  # 거리가 짧은 순으로 정렬
            count = 0
            for i in range(len(dist)):
                count += 1
                dis = dist[i]

                k = dis + 1
                cost = k*k + (k-1)*(k-1)
                if count*M >= cost:  # 수익이 보안 운영비용보다 크다면 정답에 반영
                    ans = max(ans, count)

    print(f'#{tc} {ans}')
