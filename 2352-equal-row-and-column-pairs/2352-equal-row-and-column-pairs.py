class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_map = { }
        for row in grid:
            row_tuple = tuple(row)
            row_map[row_tuple] = row_map.get(row_tuple,0)+1

        ans = 0
        n = len(grid)

        for col in range(n):
            column = [ ]
            for row in range(n):
                column.append(grid[row][col])
            ans += row_map.get(tuple(column),0)
        return ans


        