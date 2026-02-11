import sys

sys.stdin = open('sample_input.txt')

'''
2차원 리스트에 원자들이 배치되어 있고 방향을 가지고 있음 -1000 ~ 1000
한번에 동시에 1씩 방향으로 움직이고 충돌하면 에너지 방출하고 소멸
서로 동일한 x or y 좌표를 가진채 나머지 좌표가 서로 바뀌었다면 .5 초에 마주했다는 것
모든 원자의 위치가 이전과 동일하다면 더 이상 소멸하지 않는다는 뜻이니 종료
원자 1 <= N <= 1000  에너지 1 <= K <= 100
이동 방향 0, 1, 2, 3 상, 하, 좌, 우
'''
T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    atoms = []
    for _ in range(N):  # .5 충돌이 있으므로 좌표를 2배 확장해서 받음
        x, y, d, s = map(int, input().split())
        atoms.append([x * 2, y * 2, d, s])

    score = 0
    moves = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}

    for _ in range(4001):

        if len(atoms) < 2:  # 원자수가 1 이하가 되면 반복 종료
            break

        new_positions = {}  # 원자를 저장해 둘 딕셔너리

        new_atoms = []  # 이동 후 원자들의 위치 저장
        for i in range(len(atoms)):
            x, y, d, s = atoms[i]
            nx, ny = x + moves[d][0], y + moves[d][1]

            # 범위 체크 (-2000 ~ 2000)
            if -2000 <= nx <= 2000 and -2000 <= ny <= 2000:
                pos = (nx, ny)
                if pos not in new_positions:  # 처음 보는 좌표면 딕셔너리 생성
                    new_positions[pos] = []
                new_positions[pos].append([nx, ny, d, s])  # 같은 좌표면 리스트에 추가

        # 원자 이동
        atoms = []  # 다음 턴에 살아남을 원자들
        for pos in new_positions:
            group = new_positions[pos]
            if len(group) >= 2:  # 2개 이상이면
                for atom in group:
                    score += atom[3]  # 점수 합산
            else:
                # 1개뿐이면 살아남음
                atoms.append(group[0])

    print(f'#{tc} {score}')

'''
# 원자 삭제 1. .5초에 충돌하는 원자들 2. 서로 동일 좌표에서 만나 소멸하는 원자들 <- 좌표 확장 없이 하다가 실패한 흔적 
        remove = set()
        dic = {}
        new_dic = defaultdict(list)
        for i in range(len(place)):
            old = (place[i][0], place[i][1])
            new = (new_place[i][0], new_place[i][1])
            new_old = (new, old)

            if new_old in dic:
                idx = dic[new_old]
                remove.add(idx)
                remove.add(i)
                del dic[new_old]
            else:
                dic[(old, new)] = i

            new_dic[new].append(i)

        for val, ind in new_dic.items():
            if len(ind) > 1:
                remaining = [i for i in ind if i not in remove]
                if len(remaining) > 1:
                    for i in remaining:
                        remove.add(i)

        for i in list(remove):
            score += new_place[i][3]

        place = [val for idx, val in enumerate(new_place) if idx not in remove]
'''
