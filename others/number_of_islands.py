'''
Input:
    1, 0, 1
    1, 0, 0
    0, 1, 1

Output: 3
'''


class IslandCounter:
    def __init__(self, matrix):
        self.matrix = matrix
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])
        self.visited = [[False for _ in row] for row in self.matrix]
        self.num_islands = 0

    def get_num_islands(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.matrix[i][j] and not self.visited[i][j]:
                    self.num_islands += 1
                    self.do_bfs(i, j)

        return self.num_islands

    def do_bfs(self, row, col):
        stack = []
        self.visited[row][col] = True
        stack.append((row, col))
        while stack:
            current = stack.pop()
            current_row = current[0]
            current_col = current[1]
            above_row = current[0] - 1
            below_row = current[0] + 1
            left_col = current[1] - 1
            right_col = current[1] + 1
            if above_row >= 0 \
                and self.matrix[above_row][current_col] \
                and not self.visited[above_row][current_col]:
                    self.visited[above_row][current_col] = True
                    stack.append((above_row, current_col))
            if below_row < self.num_rows \
                and self.matrix[below_row][current_col] \
                and not self.visited[below_row][current_col]:
                    self.visited[below_row][current_col] = True
                    stack.append((below_row, current_col))
            if left_col >= 0 \
                and self.matrix[current_row][left_col] \
                and not self.visited[current_row][left_col]:
                    self.visited[current_row][left_col] = True
                    stack.append((current_row, left_col))
            if right_col < self.num_cols \
                and self.matrix[current_row][right_col] \
                and not self.visited[current_row][right_col]:
                    self.visited[current_row][right_col] = True
                    stack.append((current_row, right_col))


m = [[1, 0, 0, 1]
    , [1, 0, 0, 1]
    , [0, 1, 0, 1]
    , [1, 0, 1, 0]]

ic = IslandCounter(m)
print(ic.get_num_islands())
