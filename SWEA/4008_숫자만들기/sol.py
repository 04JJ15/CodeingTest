import sys
sys.stdin = open('sample_input.txt')


def make_perm(data):

    res = []  # 부호 경우의 수를 담을 리스트

    def dfs(path, dat):

        if len(path) == sum(data.values()):
            res.append(''.join(path))
            return

        for key in dat:  # 딕셔너리에 값이 남아 있을 경우
            if dat[key] > 0:
                dat[key] -= 1
                dfs(path + key, dat)  # 재귀
                dat[key] += 1

    dfs('', data.copy())
    return res


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    op_num = list(map(int, input().split()))
    num = list(map(int, input().split()))

    dic = {'+': op_num[0], '-': op_num[1], '*': op_num[2], '/': op_num[3]}

    result = make_perm(dic)

    answer = []

    for i in result:  # 계산 및 리스트에 저장
        ans = num[0]
        for j in range(len(num)-1):

            if i[j] == '+':
                ans += num[j+1]
            elif i[j] == '-':
                ans -= num[j+1]
            elif i[j] == '*':
                ans *= num[j+1]
            else:
                ans = int(ans / num[j+1])
        answer.append(ans)

    print(f'#{tc} {max(answer) - min(answer)}')
