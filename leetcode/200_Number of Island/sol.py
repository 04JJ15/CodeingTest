from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(a, b):
            queue = deque([(a, b)])
            grid[a][b] = '0'

            while queue:
                p, q = queue.popleft()
                for dy, dx in DIRS:
                    ny, nx = p + dy, q + dx
                    if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == '1':
                        grid[ny][nx] = '0'
                        queue.append((ny, nx))

        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    cnt += 1
                    bfs(i, j)

        return cnt
