# LeetCode 1306: Jump Game III (Highly Optimized Java Solution)

## Problem Description

Given an array of non-negative integers `arr` and a starting index `start`, you are initially positioned at `arr[start]`. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`. Your goal is to determine if you can reach any index with a value of `0`.

Notice that you cannot jump outside the bounds of the array at any time.

### Examples

* **Example 1:**
  * **Input:** `arr = [4,2,3,0,3,1,2]`, `start = 5`
  * **Output:** `true`
  * **Explanation:** One path to reach index 3 (value 0) is: `index 5 -> index 4 -> index 1 -> index 3`

* **Example 2:**
  * **Input:** `arr = [4,2,3,0,3,1,2]`, `start = 0`
  * **Output:** `true`
  * **Explanation:** One path to reach index 3 (value 0) is: `index 0 -> index 4 -> index 1 -> index 3`

* **Example 3:**
  * **Input:** `arr = [3,0,2,1,2]`, `start = 2`
  * **Output:** `false`
  * **Explanation:** There is no way to reach index 1 with value 0.

---

## Solution Design & Intuition

This problem can be modeled as a graph traversal where each array index represents a node, and the two possible jumps (`i + arr[i]` and `i - arr[i]`) represent directed edges. 

While a traditional Breadth-First Search (BFS) using an explicit `Queue` and a separate tracking array works perfectly, it introduces a significant performance tax on the heap due to object instantiation and memory allocations. 

This solution uses a **highly optimized Depth-First Search (DFS)** that minimizes resource overhead through two primary optimization strategies:

1. **In-Place Visited Tracking (Zero Auxiliary Space):** Instead of allocating a `boolean[] visited` array, we temporarily flip the value at the current index to a negative number (`arr[start] = -jump`). Since all valid elements in the original array are non-negative, a negative number serves as an instant flag that the index has already been visited, preventing infinite recursion cycles.
2. **Boolean Short-Circuiting:** By invoking recursive branches via a logical OR (`||`), if the first jump (`start + jump`) successfully finds a path to `0`, the second jump branch (`start - jump`) is completely skipped. This minimizes unnecessary stack calls.

---



## Code Implementation

```java
class Solution {
    /**
     * Determines if an index with value 0 can be reached from the start index.
     * 
     * @param arr   The input array of non-negative integers.
     * @param start The initial starting index.
     * @return true if an index with value 0 is reachable, false otherwise.
     */
    public boolean canReach(int[] arr, int start) {
        // 1. Base Case: Check array bounds and if the node was already visited
        if (start < 0 || start >= arr.length || arr[start] < 0) {
            return false;
        }
        
        // 2. Target Case: Successfully reached an index with value 0
        if (arr[start] == 0) {
            return true;
        }
        
        // 3. State Mutation: Cache the value and mark the index as visited
        int jump = arr[start];
        arr[start] = -jump; 
        
        // 4. Recurse: Explore both potential jump paths with short-circuiting
        return canReach(arr, start + jump) || canReach(arr, start - jump);
    }
}

```
---
## Algorithmic Approach: Optimized Graph Traversal (DFS)

To solve this problem efficiently, we can reframe it as a **Graph Traversal** problem:
* **Nodes:** Each index $i$ in the array `arr` represents a node.
* **Edges:** Each node has up to two directed edges leading to other indices: $i + arr[i]$ and $i - arr[i]$.
* **Goal:** Find if there is a valid path from the source node (`start`) to any destination node whose value is `0`.

---

### Step-by-Step State Machine Logic

The algorithm processes the problem by evaluating the state of the current index through four distinct phases:

#### 1. Boundary & Cycle Validation (The Guard)
Before performing any operations, the algorithm checks if the current index is valid. A state is invalid and immediately returns `false` if:
* The pointer goes out of bounds to the left (`start < 0`).
* The pointer goes out of bounds to the right (`start >= arr.length`).
* The current index has already been visited (`arr[start] < 0`). 

#### 2. Target Verification (The Success Base Case)
If the index passes the guard checks, the algorithm evaluates its value. If `arr[start] == 0`, we have successfully reached a target index, and the recursion unwinds by returning `true`.

#### 3. State Mutation (In-Place Tracking)
To prevent the algorithm from getting stuck in an infinite loop (e.g., jumping back and forth between two identical values), we must track visited states. 
* Instead of allocating an auxiliary `boolean[]` array, we cache the original jump value: `int jump = arr[start];`.
* We then negate the value in the actual array: `arr[start] = -jump;`. 
* Because the constraints state that all elements in the input are natively non-negative ($arr[i] \ge 0$), any negative value encountered later instantly signals a previously visited node.

#### 4. Dual-Path Exploration (Short-Circuit Recursion)
The algorithm recursively branches out into both valid choices:
* **Forward Jump:** `canReach(arr, start + jump)`
* **Backward Jump:** `canReach(arr, start - jump)`

By linking these two recursive calls with a logical OR (`||`) operator, Java utilizes **short-circuit evaluation**. If the forward jump evaluates to `true`, the CPU completely skips the backward jump calculation, saving significant execution time.

---

### Trace Example Walkthrough

Let's trace **Example 1**: `arr = [4, 2, 3, 0, 3, 1, 2]`, `start = 5`

```text
Step 1: start = 5, value = 1. Not visited. 
        Mutate index 5 to -1.
        Explore forward: 5 + 1 = 6.

Step 2: start = 6, value = 2. Not visited. 
        Mutate index 6 to -2.
        Explore forward: 6 + 2 = 8 (Out of bounds! Returns false).
        Explore backward: 6 - 2 = 4.

Step 3: start = 4, value = 3. Not visited. 
        Mutate index 4 to -3.
        Explore forward: 4 + 3 = 7 (Out of bounds! Returns false).
        Explore backward: 4 - 3 = 1.

Step 4: start = 1, value = 2. Not visited. 
        Mutate index 1 to -2.
        Explore forward: 1 + 2 = 3.

Step 5: start = 3, value = 0. Target found! Returns true.
