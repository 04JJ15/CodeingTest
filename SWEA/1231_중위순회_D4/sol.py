import sys
sys.stdin = open('input.txt')


class TreeNode:  # 트리 클래스
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder_traversal(root):  # 중위 순회 함수

    global ans
    if root:
        inorder_traversal(root.left)
        ans += root.val
        inorder_traversal(root.right)


for tc in range(1, 11):

    N = int(input())
    lis = [list(map(str, input().split())) for _ in range(N)]

    parsed = []

    for token in lis:  # 입력받은 값을 트리만들기 쉽게 파싱
        idx = int(token[0])
        value = token[1]
        left = int(token[2]) if len(token) >= 3 else None
        right = int(token[3]) if len(token) >= 4 else None

        parsed.append((idx, value, left, right))

    nodes = {}  # 트리의 정보를 저장할 딕셔너리

    for idx, value, _, _ in parsed:  # 트리 노드 생성
        nodes[idx] = TreeNode(value)

    for idx, _, left, right in parsed:  # 자식 붙이기
        if left:
            nodes[idx].left = nodes[left]
        if right:
            nodes[idx].right = nodes[right]

    root_main = nodes[1]
    ans = ""
    inorder_traversal(root_main)  # 루트노드 부터 중이 순회 시작

    print(f'#{tc} {ans}')

