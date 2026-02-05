import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M, L = map(int, input().split())

    tree = [0] * (2 * N+1) # 트리 높이를 확장하여 생성
    for _ in range(M):  # 트리의 리프값을 입력
        leaf_idx, leaf_value = map(int, input().split())
        tree[leaf_idx] = leaf_value

    for i in range(N//2, 0, -1):  # 0이 아닌 자식을 보유하고 있는 노드부터 역으로 계산
        tree[i] = tree[2*i] + tree[2*i+1]

        # 트리 높이를 확장하지 않고 조건문을 사용하기
        # left = tree[2 * i] if 2 * i <= N else 0
        # right = tree[2 * i + 1] if 2 * i + 1 <= N else 0
        # tree[i] = left + right

    print(f'#{tc} {tree[L]}')