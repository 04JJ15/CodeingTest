import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    clus = [list(map(int, input().split())) for _ in range(K)]
    mat = [[0] * N for _ in range(N)]

    for i in clus:
        mat[i[0]][i[1]] = [i[2], i[3]]

    for i in range(M):
        for j in range(len(clus)):  # 이동한 좌표를 clus에 저장
            if clus[j][3] == 1:
                clus[j][0] -= 1
            elif clus[j][3] == 2:
                clus[j][0] += 1
            elif clus[j][3] == 3:
                clus[j][1] -= 1
            else:
                clus[j][1] += 1

            # 이동 결과좌표가 0,6을 포함하고 있으면 방향을 반대로하고 미생물 절삭
            if clus[j][1] == 0 or clus[j][1] == N - 1 or clus[j][0] == 0 or clus[j][0] == N - 1:
                clus[j][2] = clus[j][2] // 2
                if clus[j][3] == 1:
                    clus[j][3] = 2
                elif clus[j][3] == 2:
                    clus[j][3] = 1
                elif clus[j][3] == 3:
                    clus[j][3] = 4
                else:
                    clus[j][3] = 3

        # clus를 순회하면서 같은 좌표를 가지고 있으면 합치고 방향은 가장 큰놈으로
        clus.sort(key=lambda x: (-x[2]))  # 미생물 수가 많은 순으로 정렬

        merged = []
        used = [False] * len(clus)

        for j in range(len(clus)):
            if used[j] or clus[j][2] == 0:  # 이미 합쳐졌거나 미생물이 0이면 스킵
                continue

            # 현재 군집의 정보
            row, col, count, direction = clus[j]

            # 같은 좌표에 있는 다른 군집들을 찾아서 합치기
            for k in range(j + 1, len(clus)):
                if not used[k] and clus[k][0] == row and clus[k][1] == col:
                    count += clus[k][2]  # 미생물 수 합치기
                    used[k] = True  # 합쳐진 군집 표시

            # 미생물이 0보다 크면 merged에 추가
            if count > 0:
                merged.append([row, col, count, direction])

        clus = merged  # 합쳐진 결과로 업데이트

    # M시간 반복이 모두 끝난 후
    total = 0
    for cluster in clus:
        total += cluster[2]  # 각 군집의 미생물 수(index 2)를 합산

    print(f'#{tc} {total}')
