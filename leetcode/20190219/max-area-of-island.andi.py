class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tiles = self.mark_area(grid, i, j)
                area = len(tiles)
                if area > max_area:
                    max_area = area
        return max_area
    def mark_area(self, grid: 'List[List[int]]', i: int, j: int) -> 'int':
        if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
            return []
        if grid[i][j] == 0:
            return []
        
        tiles = [(i, j)]
        grid[i][j] = 0
        tiles += self.mark_area(grid, i + 1, j)
        tiles += self.mark_area(grid, i - 1, j)
        tiles += self.mark_area(grid, i, j + 1)
        tiles += self.mark_area(grid, i, j - 1)
        
        return tiles