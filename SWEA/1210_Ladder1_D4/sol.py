import sys
sys.stdin = open('input.txt')


def left(le):
    if le == 0 or mat[idx[0]][le-1] == 0:
        return le
    else:
        return left(le-1)

def right(ri):
    if ri == 99 or mat[idx[0]][ri + 1] == 0:
        return ri
    else:
        return right(ri + 1)

for tc in range(10):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    idx = [99, mat[99].index(2)]

    while idx[0] != 0:
        if idx[1] != 0 and mat[idx[0]][idx[1]-1] == 1:
            idx[1] = left(idx[1])

        elif idx[1] != 99 and mat[idx[0]][idx[1]+1] == 1:
            idx[1] = right(idx[1])

        idx[0] -= 1

    print(f'#{N} {idx[1]}')



