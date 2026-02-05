import sys

sys.stdin = open('input.txt')


def inorder(idx):
    global value

    if idx > N: # 중위 순회
        return

    inorder(idx * 2)
    tree[idx] = value
    value += 1
    inorder(idx * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)  # 리스트로 크기가 N+1인 트리를 만듬
    value = 1  # 초기 숫자 1
    inorder(1)  # 루트에서 시작

    print(f'#{tc} {tree[1]} {tree[N // 2]}')
