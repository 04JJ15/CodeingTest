import sys
sys.stdin = open('sample_input.txt')


def solve(score, kal, index):

    # 다 담고도 칼로리가 안찼다면
    if index == N:
        score_list.add(score)
        return

    # 담았을 때 넘치지 않는다면 현재 재료를 선택하기
    if kal + mat[index][1] <= L:
        solve(score+mat[index][0], kal+mat[index][1], index+1)

    # 선택하지 않기
    solve(score, kal, index+1)


T = int(input())

for tc in range(1, T+1):

    N, L = map(int, input().split())
    mat = [tuple(map(int, input().split())) for _ in range(N)]  # 점수, 칼로리

    score_list = set()  # 중복 점수는 제거

    solve(0, 0, 0)  # 현재까지의 점수, 칼로리, 현재 재료

    print(f'#{tc} {max(list(score_list))}')
