import sys
sys.stdin = open('input.txt')


def swap(s, i, j):

    lis = list(s)
    lis[i], lis[j] = lis[j], lis[i]
    return ''.join(lis)


def res(string, exchange):

    record = {}

    def dfs(st, change):

        if change == 0:
            return st

        curr_state = (st, change)
        if curr_state in record:
            return record[curr_state]

        max_result = ""

        for i in range(len(st)):
            for j in range(i+1, len(st)):
                new_st = swap(st, i, j)

                result = dfs(new_st, change-1)
                if result > max_result:
                    max_result = result

        record[curr_state] = max_result
        return max_result

    return dfs(string, exchange)


T = int(input())

for tc in range(1, T+1):
    N, C = map(int, input().split())

    print(f'#{tc} {res(str(N), C)}')
