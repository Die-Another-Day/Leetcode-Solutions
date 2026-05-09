class Solution {
  public int[][] rotateGrid(int[][] grid, int k) {
    int t = 0, l = 0, b = grid.length - 1, r = grid[0].length - 1;

    while (t < b && l < r) {
      int perimeter = 2 * (b - t + 1) + 2 * (r - l + 1) - 4;
      int rot = k % perimeter;

      while (rot-- > 0) {
        int tmp = grid[t][l];

        for (int j = l; j < r; j++)
          grid[t][j] = grid[t][j + 1];

        for (int i = t; i < b; i++)
          grid[i][r] = grid[i + 1][r];

        for (int j = r; j > l; j--)
          grid[b][j] = grid[b][j - 1];

        for (int i = b; i > t; i--)
          grid[i][l] = grid[i - 1][l];

        grid[t + 1][l] = tmp;
      }

      t++;
      l++;
      b--;
      r--;
    }

    return grid;
  }
}
