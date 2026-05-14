class Solution {
  public boolean isGood(int[] nums) {
    int n = nums.length - 1;
    int[] cnt = new int[201];
    for (int v : nums) cnt[v]++;
    for (int i = 1; i < n; i++) if (cnt[i] != 1) return false;
    return cnt[n] == 2;
  }
}
