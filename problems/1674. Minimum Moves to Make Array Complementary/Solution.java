class Solution {
  public int minMoves(int[] nums, int limit) {
    int n = nums.length, ans = n;
    int[] d = new int[limit * 2 + 2];
    for (int i = 0, j = n - 1; i < j; ++i, --j) {
      int a = nums[i], b = nums[j];
      d[Math.min(a, b) + 1]--;
      d[a + b]--;
      d[a + b + 1]++;
      d[Math.max(a, b) + limit + 1]++;
    }
    for (int i = 2, moves = n; i <= limit * 2; ++i) {
      moves += d[i];
      if (moves < ans) ans = moves;
    }
    return ans;
  }
}
