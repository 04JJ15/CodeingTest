import sys
sys.stdin = open('input.txt')


def solve(cnt, idx, visited):  # 배터리 담은 횟수, 배터리를 담은 열 -> 다음 행이 됨, 방문처리
    global ans

    if cnt == N - 1:  # 전부 다 돌았다면 이전 값과 비교해서 최소값 저장
        ans = min(ans, sum(bats)+area[idx][0])

    if ans < sum(bats):  # 다 돌기 전에 이전 최소값보다 크면 가지치기
        return

    for i in range(N):
        if not visited[i]:  # 방문하지 않은 모든 영역에 대해 방문처리, 배터리 합, 재귀
            visited[i] = True
            bats.append(area[idx][i])
            solve(cnt+1, i, visited)
            visited[i] = False
            bats.pop()


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    visited = [True] + [False] * (N-1)  # 돌아와야하는 첫 열을 True 로 하고 방문 처리용 리스트 만들기

    bats = []  # 진행해가며 배터리를 담을 리스트
    ans = 1000

    solve(0, 0, visited)
    print(f'#{tc} {ans}')
