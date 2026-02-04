'''
차량 정비소에는 N개의 접수 창구와 M개의 정비 창구가 있다.
접수 창구는 1부터 N까지 번호가 붙어 있다. 정비 창구도 1부터 M까지 번호가 붙어 있다.

접수 창구 i에서 고객 한 명의 고장을 접수하는 데 걸리는 처리 시간은 ai이다. (1 ≤ i ≤ N)
정비 창구 j에서 고객 한 명의 차량을 정비하는 데 걸리는 처리 시간은 bj이다. (1 ≤ j ≤ M)
지금까지 차량 정비소를 방문한 고객은 K명이다.
고객은 도착하는 대로 1번부터 고객번호를 부여 받는다.
고객번호 k의 고객이 차량 정비소에 도착하는 시간은 tk이다. (1 ≤ k ≤ K)

접수 창구의 우선순위는 아래와 같다.
   ① 여러 고객이 기다리고 있는 경우 고객번호가 낮은 순서대로 우선 접수한다.
   ② 빈 창구가 여러 곳인 경우 접수 창구번호가 작은 곳으로 간다.

정비 창구의 우선순위는 아래와 같다.
   ① 먼저 기다리는 고객이 우선한다.
   ② 두 명 이상의 고객들이 접수 창구에서 동시에 접수를 완료하고 정비 창구로 이동한 경우,
   이용했던 접수 창구번호가 작은 고객이 우선한다.
   ③ 빈 창구가 여러 곳인 경우 정비 창구번호가 작은 곳으로 간다.

고객의 도착 시간 tk, 접수 창구의 처리 시간 ai, 정비 창구의 처리 시간 bj가 주어졌을 때,
지갑을 분실한 고객과 같은 접수 창구와 같은 정비 창구를 이용한 고객의 고객번호들을 찾아 그 합을 출력하는 프로그램을 작성하라.

만약, 그런 고객이 없는 경우 -1을 출력한다.
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    N_lis = list(map(int, input().split()))
    M_lis = list(map(int, input().split()))
    K_lis = list(map(int, input().split()))

    ans = 0
    people = []  # 고객 정보 모음
    N_wait = []  # 접수처에 들어가기 전 임시거처
    M_wait = []  # 정비처에 들어가기 전 임시거처
    N_ing = [None]*N  # 접수처
    M_ing = [None]*M  # 정비처

    for i in range(len(K_lis)):
        people.append([i, K_lis[i], None, None])  # [고객번호, 대기시간, 접수번호, 정비번호] 고객 정보 모음 리스트를 만듬

    people.sort(key=lambda x: x[1])  # people 리스트는 대기시간을 기준으로 정렬함

    # 고객 정보 모음, 접수, 정비 리스트에 고객 정보가 없을 경우 반복 종료
    while not (len(people) == 0 and N_ing.count(None) == N and M_ing.count(None) == M):

        while len(people) > 0 and people[0][1] == 0:  # 도착시간이 0이된 고객들은 N_wait 리스트로 이동함
            N_wait.append(people.pop(0))

        N_wait.sort(key=lambda x: x[0])  # N_wait 리스트는 고객번호를 기준으로 정렬함

        for i in range(len(N_ing)):
            if N_ing[i] is not None and N_ing[i][1] == 0:  # [0]부터 시작해서 None 이 아니고, 접수를 마친 고객을 M_wait 으로 이동시킴
                M_wait.append(N_ing[i])
                N_ing[i] = None
            elif N_ing[i] is not None:  # 현재 접수중인 고객의 시간을 1 감소
                N_ing[i][1] -= 1

        for i in range(len(M_ing)):
            if M_ing[i] is not None and M_ing[i][1] == 0:  # None 이 아니고, 정비를 마친 고객의 번호를 파악해 ans 에 삽입
                if M_ing[i][2]+1 == A and M_ing[i][3]+1 == B:
                    ans = ans + M_ing[i][0] + 1
                M_ing[i] = None
            elif M_ing[i] is not None:  # 현재 정비중인 고객의 시간을 1 감소
                M_ing[i][1] -= 1

        while len(N_wait) > 0 and N_ing.count(None) > 0:  # N_wait 의 길이가 0 이상이고 N_ing 에 None 이 존재할 때
            N_wait[0][1] = N_lis[N_ing.index(None)]-1   # N 으로부터 대기시간을 받아서 1 감소 후 N_ing 에 삽입
            N_wait[0][2] = N_ing.index(None)  # 접수처의 번호를 고객 정보에 삽입
            N_ing[N_ing.index(None)] = N_wait.pop(0)

        while len(M_wait) > 0 and M_ing.count(None) > 0:  # M_wait 의 길이가 0 이상이고 M_ing 에 None 이 존재할 때
            M_wait[0][1] = M_lis[M_ing.index(None)]-1  # M_lis 로부터 대기시간을 받아서 1 감소 후 M_ing 에 삽입
            M_wait[0][3] = M_ing.index(None)  # 정비처의 번호를 고객 정보에 삽입
            M_ing[M_ing.index(None)] = M_wait.pop(0)

        for i in range(len(people)):  # 도착 대기중인 고객들의 대기시간을 1 감소
            people[i][1] -= 1

    if ans == 0: # 출력 사항에 맞게 출력
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {ans}')
