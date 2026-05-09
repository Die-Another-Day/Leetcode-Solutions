# 1914. Cyclically Rotating a Grid

**Difficulty:** 🟡 Medium  
**Topics:** Array, Matrix, Simulation  
**LeetCode Link:** [1914. Cyclically Rotating a Grid](https://leetcode.com/problems/cyclically-rotating-a-grid/)

---

## 📄 Problem Statement

You are given an **m x n** integer matrix `grid`, where **m** and **n** are both **even integers**, and an integer **k**.

The matrix is composed of several concentric **layers**. A **cyclic rotation** of the matrix is performed by cyclically rotating **each layer** independently.

To cyclically rotate a layer **once**, each element moves to the position of its adjacent element in the **counter-clockwise** direction.

Return the matrix after applying **k** cyclic rotations.

---

## 🧪 Examples

### Example 1
Input: grid = [[40, 10], [30, 20]], k = 1
Output: [[10, 20], [40, 30]]

**Explanation:** The single layer rotates once counter-clockwise.  
`40 → 30 → 20 → 10 → 40`

---

### Example 2
Input: grid = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]], k = 2

Output: [[3, 4, 8, 12],
[2, 11, 10, 16],
[1, 7, 6, 15],
[5, 9, 13, 14]]


**Explanation:** After 2 counter-clockwise rotations:
- **Outer layer** (1–16 perimeter): rotates by 2 positions
- **Inner layer** (6, 7, 10, 11): rotates by 2 positions

---

## 🔒 Constraints

| Constraint | Value |
|------------|-------|
| `m == grid.length` | 2 ≤ m ≤ 50 |
| `n == grid[i].length` | 2 ≤ n ≤ 50 |
| Both `m` & `n` | **Even** integers |
| `grid[i][j]` | 1 ≤ value ≤ 5000 |
| `k` | 1 ≤ k ≤ 10⁹ |

---

## 💡 Approach & Intuition

### Core Insight

A matrix with even dimensions can be decomposed into **concentric rectangular layers**. Each layer is independent — rotating one does not affect the others.

Layer 0: (0,0) ──────────→ (0,n-1)
↑ ↓
(m-1,0) ←────────── (m-1,n-1)

Layer 1: (1,1) ──────────→ (1,n-2)
↑ ↓
(m-2,1) ←────────── (m-2,n-2)


### Why Modulo?

Each layer has a fixed **perimeter length**:
perimeter = 2 × (b - t + 1) + 2 × (r - l + 1) - 4

Rotating by `k` is equivalent to rotating by `k % perimeter`, since a full rotation (perimeter steps) brings every element back to its start.  

### Algorithm Steps  

1. **Define boundaries** — `t` (top), `b` (bottom), `l` (left), `r` (right) for the current layer  
2. **Compute effective rotations** — `rot = k % perimeter`  
3. **Rotate one position at a time** `rot` times, each shifting the perimeter clockwise:  
   - Save `grid[t][l]` (top-left corner)  
   - Shift top row: `grid[t][j] = grid[t][j+1]` ←  
   - Shift right column: `grid[i][r] = grid[i+1][r]` ↑  
   - Shift bottom row: `grid[b][j] = grid[b][j-1]` →  
   - Shift left column: `grid[i][l] = grid[i-1][

