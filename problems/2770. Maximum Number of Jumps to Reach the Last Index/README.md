# 🚀 Maximum Number of Jumps to Reach the Last Index

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-Medium-F0AD4E?style=for-the-badge" alt="Medium"/>
  <img src="https://img.shields.io/badge/Language-Java-ED8B00?style=for-the-badge&logo=java" alt="Java"/>
  <img src="https://img.shields.io/badge/Acceptance-42.1%25-4CAF50?style=for-the-badge" alt="Acceptance Rate"/>
  <img src="https://img.shields.io/badge/Time Complexity-O(n²)-blue?style=for-the-badge" alt="O(n²)"/>
  <img src="https://img.shields.io/badge/Space Complexity-O(n)-purple?style=for-the-badge" alt="O(n)"/>
</p>

---

## 📋 Problem Statement

**LeetCode 2770** — You are given a **0-indexed** array `nums` of `n` integers and an integer `target`.

You are initially positioned at **index 0**. In one step, you can jump from index `i` to any index `j` such that:

- `0 <= i < j < n`
- `-target <= nums[j] - nums[i] <= target`

Return the **maximum number of jumps** you can make to reach index `n - 1`. If it is impossible, return `-1`.

---

## 🧠 Intuition

This problem is a **dynamic programming** variant of jump-based path optimization. At its core, it asks: *What is the longest path from index 0 to index n-1, where each edge is valid only if the absolute difference between elements is within the target?*

The key insight is that we can build the solution incrementally — for each position `j`, we look back at all previous positions `i` that can jump to `j`, and take the one that gives us the longest path so far.

---

## 🔧 Algorithm

### Approach: Dynamic Programming (Bottom-Up)

We define:

> **`dp[i]`** = the maximum number of jumps required to reach index `i` from index `0`.

#### Steps:

1. **Initialize** `dp[0] = 0` (0 jumps needed to be at the start), and set all other entries to `-1` (unreachable).
2. **Iterate** over each position `j` from `1` to `n-1`.
3. For each `j`, check all previous positions `i` where `i < j`:
   - If `i` is reachable (`dp[i] != -1`) **and** the jump condition holds (`|nums[j] - nums[i]| <= target`), then update:
     - `dp[j] = max(dp[j], dp[i] + 1)`
4. **Return** `dp[n-1]`.

---

## 💻 Code

```java  
class Solution {  
  public int maximumJumps(int[] nums, int target) {  
    int n = nums.length;  
    int[] dp = new int[n];  
    Arrays.fill(dp, -1);  
    dp[0] = 0;  
    for (int j = 1; j < n; j++)  
      for (int i = 0; i < j; i++)  
        if (dp[i] != -1 && Math.abs(nums[j] - nums[i]) <= target)  
          dp[j] = Math.max(dp[j], dp[i] + 1);  
    return dp[n - 1];  
  }  
}  
