class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def split(total, n):
            q = total // n  # 몫
            r = total % n  # 나머지

            result = []
            for i in range(n):
                if i < r:
                    result.append(q + 1)
                else:
                    result.append(q)

            return result

        output = []
        length = len(words)
        pivot = 0 # 단어들 리스트의 반복 카운트

        temp = 0 # 단어 + 공백 1개도 같이 길이에 포함
        only_word = 0 # 순수 단어 만의 길이
        cnt = 0  # 한문장에 들어갈 단어 개수 세기
        while pivot < length:
            if maxWidth >= temp + len(words[pivot]):
                temp += len(words[pivot]) + 1  # 문장에 들어갈 최소 길이 : 단어 + 공백
                only_word += len(words[pivot])
                pivot += 1
                cnt += 1
            else:
                start = pivot - cnt  # 이번 문장에 들어갈 단어의 시작인덱스
                blank = maxWidth - only_word  # 이번 문장에 들어갈 빈칸 길이

                if cnt == 1:  # 만약 단어가 1개라면
                    output.append(words[start] + " " * blank)
                else:
                    res = split(blank, cnt - 1)
                    out_str = words[start]
                    for i in range(len(res)):
                        out_str = out_str + " " * res[i] + words[start + i + 1]
                    output.append(out_str)

                cnt = 0
                only_word = 0
                temp = 0

        # 마지막 줄 처리
        start = pivot - cnt
        out_str = ""
        right_blank = maxWidth - only_word - cnt + 1
        for i in range(cnt):
            out_str = out_str + words[start + i] + " "
        out_str = out_str[:len(out_str) - 1] + " " * right_blank
        output.append(out_str)

        return output
