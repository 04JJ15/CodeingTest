import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    st = ''.join(input().split())

    result = 0  # 토막난 막대기의 총 개수
    stack = []
    iron = []  # 1개의 막대기가 몇 개로 토막나는지 저장

    for i in st:
        if i == '(':  # 열린괄호를 만나면 스택에 추가하고 iron 리스트에 0을 추가
            stack.append(i)
            iron.append(0)
        else:
            if iron[-1] == 0:  # 닫힌괄호를 만났을 때 iron 의 LI 가 0이라면 레이저
                iron.pop(-1)  # iron 의 LI 를 pop 하고 모든 iron 의 값에 1 추가
                iron = [x + 1 for x in iron]
            else:
                result += (iron.pop(-1)+1)  # 그게 아니라면 막대기이니 pop 하면서 result 에 막대기 개수 추가
            stack.pop(-1)  # 스택에서 열린괄호 제거

    print(f'#{tc} {result}')