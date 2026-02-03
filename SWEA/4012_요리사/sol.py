'''
N개의 식재료가 있다.

식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)

이때, 각각의 음식을 A음식, B음식이라고 하자.

비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야 한다.

음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게 된다.

식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다. (1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)

각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합이다.

세로축으로 i번째 위치에 있고 가로축으로 j번째 위치에 있는 값이 Sij이다.



식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고,
가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때, 두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open('sample_input.txt')

# 조합 구하는 함수
def comb(arr, n):
    result = []

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]

        for rest in comb(arr[i + 1:], n - 1):
            result.append([elem] + rest)

    return result

# 순열 구하는 함수
def perm(arr, n):
    result = []

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]

        for rest in comb(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + rest)

    return result

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    mid = N // 2

    lis = comb([a for a in range(0, N-1)], mid) # 조합을 통해 A음식 리스트를 뽑아온다

    for i in lis:
        ingredient = [] # A음식 리스트를 순회할 때 나머지 음식으로 요리할 B음식 리스트를 만든다
        for j in range(N):
            if j not in i:
                ingredient.append(j)

        sum1, sum2 = 0, 0

        for j in perm(i, 2): # A음식 리스트로 2 순열을 만들고 순회하며 점수table의 점수대로 더한다
            sum1 += mat[j[0]][j[1]]

        for j in perm(ingredient, 2): # B음식 리스트로 2 순열을 만들고 순회하며 점수table의 점수대로 더한다
            sum2 += mat[j[0]][j[1]]

        ans.append(abs(sum1-sum2)) # 절대값차이를 ans 리스트에 저장하고 그중 최소값을 출력한다

    print(f'#{tc} {min(ans)}')




