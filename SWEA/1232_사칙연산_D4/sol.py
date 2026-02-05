import sys
sys.stdin = open('input.txt', 'r')


def calc(v):
    curr_node = tree[v] # 트리로부터 현재 노드의 정보를 가져옴

    if len(curr_node) == 2:  # 길이가 2라면 숫자라는 뜻
        return float(curr_node[1])

    left_child_idx = int(curr_node[2]) # 연산자라면 자식 노드의 인덱스를 변수에 저장
    right_child_idx = int(curr_node[3])

    left_val = calc(left_child_idx) # 왼쪽부터 재귀를 수행
    right_val = calc(right_child_idx)

    oper = curr_node[1]

    if oper == '+':
        return left_val + right_val
    elif oper == '-':
        return left_val - right_val
    elif oper == '*':
        return left_val * right_val
    elif oper == '/':
        return left_val / right_val


for tc in range(1, 11):
    N = int(input())
    tree = [0] + [list(map(str, input().split())) for _ in range(N)]
    result = calc(1)

    print(f'#{tc} {int(result)}')
