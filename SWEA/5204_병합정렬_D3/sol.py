import sys
sys.stdin = open('input.txt')

from collections import deque


def merge(left, right):
    ans = []
    left = deque(left)
    right = deque(right)

    if left[-1] > right[-1]:
        cnt[0] += 1

    while left and right:
        if left[0] < right[0]:
            ans.append(left.popleft())
        else:
            ans.append(right.popleft())

    ans.extend(left)
    ans.extend(right)

    return ans


def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = [0]

    lis = merge_sort(num_list)

    print(f'#{tc} {lis[N//2]} {cnt[0]}')
