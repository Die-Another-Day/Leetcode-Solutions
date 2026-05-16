class Solution {
  public int findMin(int[] nums) {
    int l = 0, r = nums.length - 1, m;

    while (l < r) {
      m = (l + r) >>> 1; // 1. Prevents integer overflow & executes faster
      
      if (nums[m] == nums[r]) --r;
      else if (nums[m] < nums[r]) r = m;
      else l = m + 1;
    }

    return nums[l];
  }
}
