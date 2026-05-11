# 2553. Separate the Digits in an Array

## Problem Description

**Difficulty:** Easy  
**Topics:** Array, Simulation  

Given an array of positive integers `nums`, return an array `answer` that consists of the digits of each integer in `nums` after separating them **in the same order** they appear in `nums`.

To separate the digits of an integer means to get all the digits it has in the same order.

### Examples

**Example 1:**

```
Input:  nums = [13, 25, 83, 77]
Output: [1, 3, 2, 5, 8, 3, 7, 7]
```

- The separation of `13` is `[1, 3]`
- The separation of `25` is `[2, 5]`
- The separation of `83` is `[8, 3]`
- The separation of `77` is `[7, 7]`

**Example 2:**

```
Input:  nums = [7, 1, 3, 9]
Output: [7, 1, 3, 9]
```

- Each integer is already a single digit, so the separation is the integer itself.

### Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`

---

## Approach

### Intuition

Iterate through each number in the array, extract its decimal digits from most significant to least significant, and append them to a result list.

### Solutions

#### Solution 1: List + String Conversion (Simple)

```java
class Solution {
  public int[] separateDigits(int[] nums) {
    List<Integer> ans = new ArrayList<>();

    for (final int num : nums)
      for (final char c : String.valueOf(num).toCharArray())
        ans.add(c - '0');

    return ans.stream().mapToInt(Integer::intValue).toArray();
  }
}
```

**Time Complexity:** O(n × d), where `n` is `nums.length` and `d` is the average number of digits (max 6 since `nums[i] ≤ 10^5`).

**Space Complexity:** O(n × d) for the result.

#### Solution 2: Stream Pipeline (Concise)

```java
class Solution {
  public int[] separateDigits(int[] nums) {
    return java.util.Arrays.stream(nums)
        .flatMap(num -> String.valueOf(num).chars())
        .map(c -> c - '0')
        .toArray();
  }
}
```

Same complexity, but written as a single stream pipeline without an explicit intermediate list.

---

## Key Points

- The order of digits matters — digits from earlier numbers appear before digits from later numbers.
- Each integer's digits must appear in their original most-significant-to-least-significant order.
- String conversion is the simplest approach; a purely arithmetic approach (using division and modulo) is also possible but more verbose.
