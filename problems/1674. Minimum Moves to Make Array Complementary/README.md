# 1674 Minimum Moves to Make Array Complementary

<p>
  <img src="https://img.shields.io/badge/LeetCode-1674-yellow?style=flat-square&logo=leetcode"/>
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Language-Java-blue?style=flat-square&logo=java"/>
  <img src="https://img.shields.io/badge/Time-O(n+limit)-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Space-O(limit)-brightgreen?style=flat-square"/>
</p>

---

## Problem Statement

You are given an integer array `nums` of **even length** `n` and an integer `limit`. In one move, you can replace any element with another integer between `1` and `limit` (inclusive).

The array is **complementary** if for all indices `i`, `nums[i] + nums[n - 1 - i]` equals the **same target sum**.

Return the **minimum number of moves** required to make `nums` complementary.

---

## Examples

### Example 1
Input: nums = [1, 2, 4, 3], limit = 4

Output: 1

Change `nums[2]` from `4` to `2` → `[1, 2, 2, 3]`. All pairs sum to `4`.

### Example 2
Input: nums = [1, 2, 2, 1], limit = 2

Output: 2

Change two elements, e.g., `[2, 2, 2, 2]`. All pairs sum to `4`.

### Example 3
Input: nums = [1, 2, 1, 2], limit = 2

Output: 0

Already complementary — all pairs sum to `3`.  

---  

## Constraints  

- `n == nums.length`, `2 <= n <= 10^5`  
- `1 <= nums[i] <= limit <= 10^5`  
- `n` is **even**  

---  

## Approach: Difference Array (Sweep Line)  

### Intuition  

The array is divided into `n / 2` pairs: `(nums[0], nums[n-1]), (nums[1], nums[n-2]), ...`. We choose a target sum `T` (between `2` and `2 * limit`) and modify pairs to sum to `T`.  

For a single pair `(a, b)` with `a <= b`:  

| Target `T` Range | Moves | Why |  
|---|---|---|  
| `T < a + 1` | **2** | Both must be changed |  
| `a + 1 <= T < a + b` | **1** | Change the larger element |  
| `T = a + b` | **0** | Already correct |  
| `a + b < T <= b + limit` | **1** | Change the smaller element |  
| `T > b + limit` | **2** | Both must be changed |  

A brute force checking every `T` would cost `O(n * limit)` — too slow for `10^5`.  

### Key Idea  

We use a **difference array** (sweep line) to track how the required moves change as `T` increases. Instead of recomputing for each `T`, we record **transition points** per pair and sweep once.  

For each pair `(a, b)` (assume `a <= b`):  

| Transition at `T` | Delta | Meaning |  
|---|---|---|  
| `a + 1` | `-1` | 2 moves → 1 move |  
| `a + b` | `-1` | 1 move → 0 moves |  
| `a + b + 1` | `+1` | 0 moves → 1 move |  
| `b + limit + 1` | `+1` | 1 move → 2 moves |  

### Algorithm  

1. Initialize difference array `d[0 .. 2*limit+1]` to zeros.  
2. For each pair `(a, b)`:  
   - `d[min(a,b) + 1]--`  
   - `d[a + b]--`  
   - `d[a + b + 1]++`  
  
