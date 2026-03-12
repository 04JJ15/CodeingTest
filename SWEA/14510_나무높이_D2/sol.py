import sys
sys.stdin = open('Sample_input.txt')

# 홀수 날은 키가 1 짝수날은 키가 2 한개의 나무만 물을 줄 수 있음, 물을 안 줘도됨 가중 큰 나무와 같아지도록
# 1을 더 많이 요구하는 경우는 어카지?

T = int(input())

for tc in range(1, T+1):

    N = int(input())  # 나무의 개수
    height = list(map(int, input().split()))  # 나무들의 높이

    goal = max(height)
    diff = [goal - height[i] for i in range(len(height))]  # 최고 높이에서 차를 담은 리스트
    ans = 0
    cnt_odd = 0
    su = 0

    for i in range(len(height)):  # 1을 무조건 요구하는 나무들의 개수를 구하고 짝수화
        if diff[i] % 2 == 1:
            diff[i] -= 1
            cnt_odd += 1

    if cnt_odd == 0:  # 1을 요구하는 나무가 없을 때
        if sum(diff) == 0:  # 차 또한 0이라면
            ans = 0
        else:
            su = sum(diff)  # 차의 합이 0이 아니라면
            ans += (su // 3) * 2  # 2일연속 물주는 날과

            if su % 3 == 1:  # 나머지 물을 줘야하는 날을 더한다
                ans += 1
            elif su % 3 == 2:
                ans += 2
    else:  # 1을 요구하는 나무가 있을 때
        if sum(diff) == 0:  # 차의 합이 0이라면
            ans = (cnt_odd - 1) * 2 + 1  # 사이에 2만큼 물주는 날에 물을 안주면됨
        else:  # 차의 합이 0이 아니라면
            su = sum(diff) - (cnt_odd - 1) * 2  # 일단 사이에 2만큼 물주는 날을 차의 합에서 뺌
            if su <= 0:
                ans = (cnt_odd - 1) * 2 + 1  # 그렇게 해서 0보다 작아지면 그만큼의 1만 필수적으로 필요했던거임
            else:
                ans = cnt_odd * 2  # 그게 아니면 2만큼 물을 줘서 다시 1,2의 사이클로 시작하게 해주고
                su -= 2

                ans += (su // 3)*2  # 2일연속 물주는 날과

                if su % 3 == 1:  # 나머지 물주는 날을 구한다
                    ans += 1
                elif su % 3 == 2:
                    ans += 2

    print(f'#{tc} {ans}')
