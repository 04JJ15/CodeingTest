'''헌터

헌터는 (0,0)위치에서 고객이 의뢰한 몬스터를 처치하고 고객에게 처치 사실을 알린다
헌터는 상하좌우로 한칸씩 움직인다
처리하고 곧바로 확인 받으로 가지 않아도 된다
몬스터의 좌표에 도달하는 것이 처치, 고객의 좌표에 도달하는 것이 확인
몬스터는 양수 고객은 몬스터 값의 음수이다
0이면 그곳은 빈곳
최소 경로로 모든 몬스터를 처치하고 고객에게 알리는 경우의 이동거리를 구하라

'''

import sys
sys.stdin = open('sample_input.txt')


def solve(row, col):

    global dist, cnt, ans

    if cnt == len(place):  # 영역을 방문한 횟수
        ans = min(ans, dist)
        return

    for pla in place:
        if place[pla][2] and place[pla][3] is False:  # 현재 방문 가능하다면
            dist += (abs(row - place[pla][0]) + abs(col - place[pla][1]))  # 이동 하고
            place[pla][3] = True  # 방문하고
            if pla > 0:  # 몬스터 였다면
                place[-pla][2] = True  # 고객 방문 가능으로 전환
            cnt += 1

            solve(place[pla][0], place[pla][1])

            dist -= (abs(row - place[pla][0]) + abs(col - place[pla][1]))  # 제자리로 돌아오고
            place[pla][3] = False  # 방문 취소
            if pla > 0:  # 고객 방문 가능 여부도 취소
                place[-pla][2] = False
            cnt -= 1


test_case = int(input())

for tc in range(1, test_case+1):

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 모든 고객, 몬스터의 좌표를 담은 딕셔너리 만들기, boolean 처리를 통해 현재 방문할 수 있는지를 확인, 헌터가 방문했는지
    place = {}

    for i in range(N):
        for j in range(N):
            if mat[i][j] < 0:
                place[mat[i][j]] = [i, j, False, False]
            elif mat[i][j] > 0:
                place[mat[i][j]] = [i, j, True, False]

    cnt = 0
    dist = 0
    ans = 1000000000

    solve(0, 0)

    print(f'#{tc} {ans}')
