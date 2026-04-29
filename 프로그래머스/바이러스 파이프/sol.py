from collections import deque


def solution(n, infection, edges, k):
    def bfs(inf_set, pipe):
        new_set = set(inf_set)

        queue = deque([node for node in inf_set])
        while queue:
            node = queue.popleft()

            for n, t in graph[node]:
                if t == pipe and n not in new_set:
                    new_set.add(n)
                    queue.append(n)

        return new_set

    def dfs(infection_set, cnt):

        if cnt == 0:
            return len(infection_set)

        max_inf = len(infection_set)
        for pipe in [1, 2, 3]:
            new_infection_set = bfs(infection_set, pipe)
            if new_infection_set == infection_set:
                continue
            max_inf = max(max_inf, dfs(new_infection_set, cnt - 1))

        return max_inf

    graph = [[] for _ in range(n + 1)]
    for x, y, t in edges:
        graph[x].append((y, t))
        graph[y].append((x, t))

    answer = dfs({infection}, k)
    return answer
