class Solution {
  public int minimumEffort(int[][] tasks) {
    Arrays.sort(tasks, (a, b) -> (a[0] - a[1]) - (b[0] - b[1]));
    int ans = 0, cur = 0;
    for (var t : tasks) {
      if (cur < t[1]) { ans += t[1] - cur; cur = t[1]; }
      cur -= t[0];
    }
    return ans;
  }
}
