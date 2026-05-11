class Solution {
  public int[] separateDigits(int[] nums) {
    return java.util.Arrays.stream(nums)
        .flatMap(num -> String.valueOf(num).chars())
        .map(c -> c - '0')
        .toArray();
  }
}
