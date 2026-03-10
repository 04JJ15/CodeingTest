import sys
sys.stdin = open('input.txt')


def solve(start, count):
    global ans

    if ans <= count:  # 이전 최소값보다 크면 가지치기
        return

    for i in range(start, 100):  # 모든 원소를 좌 상단을 기준으로 반복
        a, b = i // 10, i % 10
        if matrix[a][b] == 1:  # 1인 칸을 찾으면
            for num in range(5, 0, -1):
                if check(a, b, num) and paper[num] > 0:  # 종이를 붙일 수 있나 확인하고
                    push_pop(a, b, num, 0)  # 종이 붙이기
                    paper[num] -= 1  # 종이 -1
                    solve(i+1, count+1)  # 백트레킹
                    push_pop(a, b, num, 1)
                    paper[num] += 1
            return

    ans = min(ans, count)


def check(a, b, num):  # 가능한지 확인
    if a + num - 1 >= 10 or b + num - 1 >= 10:
        return False
    su = 0
    for i in range(num):
        su += sum(matrix[a+i][b:b+num])

    if su == num**2:
        return True
    else:
        return False


def push_pop(a, b, num, pk):  # 붙이고 때고
    if pk == 0:
        for i in range(num):
            for j in range(num):
                matrix[a+i][b+j] = 0
    else:
        for i in range(num):
            for j in range(num):
                matrix[a+i][b+j] = 1


matrix = [list(map(int, input().split())) for _ in range(10)]

paper = [5]*6  # 색종이 갯수
ans = 26  # 붙인 색종이 갯수

solve(0, 0)
if ans == 26:
    print(-1)
else:
    print(ans)
