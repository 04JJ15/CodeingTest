'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
예를 들어
“3+4+5+6+7”
라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
"34+5+6+7+"
변환된 식을 계산하면 25를 얻을 수 있다.
문자열 계산식을 구성하는 연산자는 + 하나뿐이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 문자열 계산식의 길이가 주어진다. 그 다음 줄에 문자열 계산식이 주어진다.
총 10개의 테스트 케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):

    N = int(input())
    cond = str(input())

    sign = ""  # 부호를 저장할 문자열
    post_cond = ""  # post_fix 로 저장할 문자열

    # post_fix 변환
    for i in cond:
        if i.isdecimal():
            post_cond += i
        else:
            sign += i
    post_cond += sign

    stack = []

    for i in range(len(post_cond)):
        if post_cond[i] != '+':  # 부호가 아니면 stack 에 푸쉬
            stack.append(int(post_cond[i]))
        else:  # 부호면 stack 에서 2개 pop 해서 합치고 다시 push
            stack.append(stack.pop(-1) + stack.pop(-1))

    result = stack.pop(0)
    print(f'#{tc} {result}')

