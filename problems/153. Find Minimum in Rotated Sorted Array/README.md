# 153. Find Minimum in Rotated Sorted Array

## 📌 Table of Contents
1. [Problem Overview](#problem-overview)
2. [Problem Analysis](#problem-analysis)
3. [The Rotated Array Mechanics](#the-rotated-array-mechanics)
4. [Solution Approaches](#solution-approaches)
    - [Brute Force (Linear Search)](#1-brute-force-linear-search)
    - [Optimized (Binary Search)](#2-optimized-binary-search)
5. [Detailed Logic Explanation](#detailed-logic-explanation)
6. [Step-by-Step Dry Run](#step-by-step-dry-run)
7. [Code Implementation](#code-implementation)
8. [Complexity Analysis](#complexity-analysis)
9. [Edge Cases & Constraints](#edge-cases--constraints)
10. [Frequently Asked Questions](#frequently-asked-questions)

---

## 📝 Problem Overview

The problem asks us to find the minimum element in an array that was originally sorted in ascending order but has been "rotated" some number of times.

**Definition of Rotation:**
If we have an array `[a[0], a[1], ..., a[n-1]]`, one rotation results in `[a[n-1], a[0], a[1], ..., a[n-2]]`.

### Constraints:
- The array contains **unique** elements.
- The time complexity must be **$O(\log n)$**.
- The array length $n$ is between $1$ and $5000$.

---

## 🔍 Problem Analysis

In a standard sorted array, the minimum element is always at the first index (`index 0`). However, rotation shifts the smallest value to some "pivot point" $i$.

### Example:
- **Original:** `[1, 2, 3, 4, 5, 6, 7]`
- **Rotated 4 times:** `[4, 5, 6, 7, 1, 2, 3]`

The goal is to find `1` in $O(\log n)$ time. Since $O(\log n)$ is required, we cannot simply iterate through the array. We **must** use a variation of Binary Search.

---

## ⚙️ The Rotated Array Mechanics

When a sorted array is rotated, it splits into two sorted subarrays:
1.  **Left Subarray:** `[4, 5, 6, 7]` (All elements are $>=$ the first element of the original).
2.  **Right Subarray:** `[1, 2, 3]` (All elements are $<$ the first element of the original).

The minimum element is the **first element of the right subarray**.

### Property of Binary Search here:
- If `nums[mid] > nums[right]`: The minimum must be to the **right** of `mid`.
- If `nums[mid] < nums[right]`: The minimum is either at `mid` or to the **left** of `mid`.

---

## 🚀 Solution Approaches

### 1. Brute Force (Linear Search)
We could iterate through the array and find the smallest number.
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$
- **Verdict:** Fails the $O(\log n)$ requirement.

### 2. Optimized (Binary Search)
By comparing the middle element with the boundaries, we can discard half of the search space in every iteration.
- **Time Complexity:** $O(\log n)$
- **Space Complexity:** $O(1)$
- **Verdict:** Ideal Solution.

---

## 💡 Detailed Logic Explanation

The algorithm maintains two pointers: `l` (left) and `r` (right).

1.  Calculate `mid = (l + r) / 2`.
2.  **Compare `nums[mid]` with `nums[r]`**:
    - **Why `nums[r]`?** Because the rightmost element is the most reliable indicator of whether the rotation "inflection point" has occurred.
    - If `nums[mid]` is greater than `nums[r]`, it implies the "drop" (the minimum) occurs somewhere after `mid`. Therefore, we move our left pointer: `l = mid + 1`.
    - If `nums[mid]` is less than `nums[r]`, it implies the right side is perfectly sorted, meaning `mid` could be the minimum or the minimum is to the left. We move our right pointer: `r = mid`.
3.  The loop continues as long as `l < r`.
4.  When `l == r`, the pointers have converged on the smallest value.

---

## 📑 Step-by-Step Dry Run

**Input:** `nums = [4, 5, 6, 7, 0, 1, 2]`

### Iteration 1:
- `l = 0`, `r = 6`
- `mid = (0 + 6) / 2 = 3`
- `nums[mid] = 7`, `nums[r] = 2`
- Since `7 > 2`, the minimum is to the right.
- `l = mid + 1 = 4`

### Iteration 2:
- `l = 4`, `r = 6`
- `mid = (4 + 6) / 2 = 5`
- `nums[mid] = 1`, `nums[r] = 2`
- Since `1 < 2`, the minimum could be `mid` or to the left.
- `r = mid = 5`

### Iteration 3:
- `l = 4`, `r = 5`
- `mid = (4 + 5) / 2 = 4`
- `nums[mid] = 0`, `nums[r] = 1`
- Since `0 < 1`, `r = mid = 4`

### Result:
- `l = 4`, `r = 4`. Loop breaks.
- Return `nums[4]` which is `0`.

---

## 💻 Code Implementation

```java
/**
 * Java Solution for Find Minimum in Rotated Sorted Array.
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
class Solution {
    public int findMin(int[] nums) {
        // Initialize pointers
        int l = 0;
        int r = nums.length - 1;

        // Binary search loop
        while (l < r) {
            // Find middle index
            int m = (l + r) / 2;

            // If middle element is greater than rightmost, 
            // the pivot point (minimum) is in the right half.
            if (nums[m] > nums[r]) {
                l = m + 1;
            } 
            // Otherwise, the minimum is in the left half (including mid).
            else {
                r = m;
            }
        }

        // Both pointers converge to the minimum element
        return nums[l];
    }
}
