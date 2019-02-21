class Solution {
  public int maxAreaOfIsland(int[][] grid) {
      int maxArea = 0;
      for (int i = 0; i < grid.length; i++) {
          for (int j = 0; j < grid[i].length; j++) {
              final int markedArea = markArea(grid, i, j);
              if (markedArea > maxArea) {
                  maxArea = markedArea;
              }
          }
      }
      return maxArea;
  }
  
  private int markArea(int[][] grid, int i, int j) {
      if (i >= grid.length || i < 0 || j >= grid[i].length || j < 0) {
          return 0;
      }
      if (grid[i][j] == 0) {
          return 0;
      }
      grid[i][j] = 0;
      return 1 + markArea(grid, i + 1, j) + markArea(grid, i - 1, j)
          + markArea(grid, i, j + 1) + markArea(grid, i, j - 1);
  }
}