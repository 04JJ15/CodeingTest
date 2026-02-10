import sys
sys.stdin = open('sample_input.txt')

'''
주차장 크기는 1~n 최대 100 차는 최대 2000대
빈 공간이 없다면 대기 -> 공간이 생기면 순차적으로 주차
빈 공간이 있으면 가장 작은 번호에 주차
주차 요금: 차량 무게 * 주차 번호
m대의 차량이 들어오고 나감 -> 총 수입 구하기 
'''

from collections import deque
import heapq


def solve():

    p_spot = [i for i in range(n)]  # 주차 공간, 이 리스트 안에 있으면 비어있음
    wait_list = deque()  # 대기열
    revenue = 0  # 수익
    dic = {}  # 차량번호 : 주차번호 저장 딕셔너리
    cnt = 0  # 차 카운트

    for curr in in_and_out:

        if curr > 0:  # 차가 들어오는 거라면

            if p_spot:  # 주차 공간이 비어 있다면
                idx = heapq.heappop(p_spot)  # 채워준다/ 힙은 비워준다
                dic[curr] = idx  # 어떤 차가 어디에 주차했는지 딕셔너리에 저장
                revenue += fee[idx] * car_weight[curr]  # 수익 반영
                cnt += 1
            else:  # 가득 찼다면
                wait_list.append(curr)  # 대기열에 저장
        else:  # 차가 나가는 경우
            out_car_num = -curr  # 어떤 차가 나가는지
            out_car_index = dic.pop(out_car_num)  # 어떤 번호에서 나가는지
            if wait_list:  # 대기열이 존재한다면
                num = wait_list.popleft()  # 하나 뽑아와서
                dic[num] = out_car_index  # 차량 번호만 교체해준다
                revenue += fee[out_car_index] * car_weight[num]  # 수익 반영
                cnt += 1
            else:  # 대기열이 없다면
                heapq.heappush(p_spot, out_car_index)  # 비워준다/ 힙에 채워준다

        if cnt == m:  # 차가 나갈 일만 남았다면 조기종료
            break

    return revenue


T = int(input())

for tc in range(1, T+1):

    n, m = map(int, input().split())  # 주차 공간, 총 차량 수

    fee = [int(input()) for _ in range(n)]  # 주차 공간 별 요금
    car_weight = [0] + [int(input()) for _ in range(m)]  # 차들의 무게 0번 차는 없음
    in_and_out = deque(int(input()) for _ in range(2*m))  # 차들의 오고 가는 순서 양수면 들어오고 음수면 나감

    print(f'#{tc} {solve()}')
