import sys
sys.stdin = open('sample_input.txt')

def babygin(cards):
    nums = [0] * 10

    for card in cards:
        nums[card] += 1

    # triplet 체크
    for i in range(10):
        if nums[i] >= 3:
            return True

    # run 체크
    for i in range(8):
        if nums[i] >= 1 and nums[i + 1] >= 1 and nums[i + 2] >= 1:
            return True

    return False

T = int(input())

for tc in range(1, T+1):
    card_list = list(map(int, input().split()))
    ans = 0
    A = []
    B = []

    for i in range(0, 12, 2):
        A.append(card_list[i])
        if len(A) >= 3 and babygin(A):
            ans = 1
            break
        B.append(card_list[i+1])
        if len(B) >= 3 and babygin(B):
            ans = 2
            break

    print(f'#{tc} {ans}')
