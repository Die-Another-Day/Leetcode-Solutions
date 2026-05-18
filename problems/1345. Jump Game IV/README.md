# LeetCode 1345: Jump Game IV (Highly Optimized Java Solution)

## Problem Description

Given an array of integers `arr`, you are initially positioned at the first index ($0$-indexed) of the array. In one step, you can jump from your current index `i` to any of the following indices:

1. **`i + 1`** (Forward step) where `i + 1 < arr.length`.
2. **`i - 1`** (Backward step) where `i - 1 >= 0`.
3. **`j`** (Value-identical step) where `arr[i] == arr[j]` and `i != j`.

Return the **minimum number of steps** required to reach the last index of the array (`arr.length - 1`). You are guaranteed not to step outside the array boundaries.

### Examples

* **Example 1:**
  * **Input:** `arr = [100,-23,-23,404,100,23,23,23,3,404]`
  * **Output:** `3`
  * **Explanation:** Index `0` ($\text{value } 100$) $\rightarrow$ Index `4` ($\text{value } 100$) $\rightarrow$ Index `3` ($\text{value } 404$) $\rightarrow$ Index `9` ($\text{value } 404$).

* **Example 2:**
  * **Input:** `arr = [7]`
  * **Output:** `0`
  * **Explanation:** You are already at the destination index.

---

## Algorithmic Approach & Core Concepts

This problem maps directly to finding the **shortest path in an unweighted graph**, which makes **Breadth-First Search (BFS)** the ideal algorithmic framework. Each index represents a node, and the valid jump options represent the graph's directed edges. 

However, a native BFS implementation will result in a **Time Limit Exceeded (TLE)** error on large datasets containing heavily repeated values (e.g., `[7, 7, 7, ..., 7]`). If an array contains thousands of identical values, processing matching transitions over and over yields an $\mathcal{O}(n^2)$ complexity. This optimized solution incorporates specific algorithmic adjustments to guarantee a strict linear execution time.

### Key Optimization Mechanics

1. **Graph Map Clearing (`graph.remove`):** This is the single most critical structural micro-optimization. The first time the algorithm explores a value group via `graph.get(arr[i])`, it finds all target nodes with that identical value and pushes them into the queue. Right after processing this list, we call `graph.remove(arr[i])`. This ensures that subsequent iterations encountering the same value completely bypass rewriting or iterating over those redundant value-identical edges, capping edge processing to exactly once.
2. **Immediate "Seen" Guarding:** Instead of marking a node as visited after it is pulled from the queue (`q.poll()`), this solution marks the index as true (`seen[nextIdx] = true`) *immediately* before invoking `q.offer()`. This blocks duplicate indices from entering the queue multiple times during a single step traversal.
3. **Pre-sized Map Allocation:** Initializing the `HashMap` with an explicit capacity equal to `n` minimizes dynamic internal bucket rehashing overhead within the JVM.

---

## Code Implementation

```java
import java.util.*;

class Solution {
    public int minJumps(int[] arr) {
        int n = arr.length;
        if (n <= 1) return 0;

        // 1. Pre-allocate map with expected capacity to eliminate resize overhead
        Map<Integer, List<Integer>> graph = new HashMap<>(n);
        for (int i = 0; i < n; i++) {
            graph.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }

        // 2. Continuous primitive tracking and BFS queue allocations
        Queue<Integer> q = new ArrayDeque<>();
        boolean[] seen = new boolean[n];
        
        q.offer(0);
        seen[0] = true;
        int steps = 0;

        // 3. Layer-by-Layer BFS Traversal
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0) {
                int i = q.poll();

                // Base Case: Target reached
                if (i == n - 1) return steps;

                // Option A: Value-identical jumps
                List<Integer> sameValues = graph.get(arr[i]);
                if (sameValues != null) {
                    for (int nextIdx : sameValues) {
                        if (!seen[nextIdx]) {
                            seen[nextIdx] = true; // Guard immediately on entry
                            q.offer(nextIdx);
                        }
                    }
                    // CRITICAL TIME REDUCTION: Drop map entries to prevent O(N^2) processing loop
                    graph.remove(arr[i]);
                }

                // Option B: Step Forward (i + 1)
                if (i + 1 < n && !seen[i + 1]) {
                    seen[i + 1] = true;
                    q.offer(i + 1);
                }

                // Option C: Step Backward (i - 1)
                if (i - 1 >= 0 && !seen[i - 1]) {
                    seen[i - 1] = true;
                    q.offer(i - 1);
                }
            }
            steps++;
        }

        return -1;
    }
}
```

---

### Complexity Analysis

To properly evaluate the efficiency of this optimized Breadth-First Search (BFS) solution, we analyze both time and space complexities. Thanks to strategic pruning, the solution circumvents the typical pitfalls of exploring highly connected components in a graph.

---

### Time Complexity: $\mathcal{O}(n)$

The time complexity of a standard Breadth-First Search is typically expressed as $\mathcal{O}(V + E)$, where $V$ is the number of vertices (nodes) and $E$ is the number of edges (connections). In this problem:
* **Vertices ($V$):** Exactly $n$, corresponding to each index in the input array `arr`.
* **Edges ($E$):** In a worst-case input where all elements share the same value (e.g., `[7, 7, 7, ..., 7]`), a naive graph construction creates a fully connected clique. This would result in $n \times (n - 1)$ edges, driving a basic BFS down to a sluggish $\mathcal{O}(n^2)$ time complexity.

#### Why This Solution Achieves $\mathcal{O}(n)$ Linear Time:
1. **Graph Population:** Building the adjacency list via the `HashMap` takes a single pass over the array, taking exactly $\mathcal{O}(n)$ time.
2. **Immediate Step Guarding:** By checking and marking indices as visited (`seen[nextIdx] = true`) right at the moment they are offered to the queue rather than when they are polled, we guarantee that no individual index is ever inserted into the queue more than once.
3. **Aggressive Edge Pruning (`graph.remove`):** The first time any node of a specific value is processed, the algorithm iterates through all other indices sharing that exact value. Immediately following this loop, `graph.remove(arr[i])` deletes the entry from the map. Any future node processed with the same value will find a `null` list and skip the redundant inner loop entirely. 

As a result, every node is added to the queue at most once, and the group of value-identical edges is traversed exactly once across the entire lifecycle of the program. This locks the total time complexity to a strict $\mathcal{O}(n)$.

---

### Space Complexity: $\mathcal{O}(n)$

The memory footprint is scaled linearly with respect to the size of the input array due to the allocation of three primary structures:

1. **Adjacency List Map (`graph`):** The `HashMap` stores each unique integer value from the array as a key, mapped to a list of its respective indices. Collectively, across all keys, the total number of items stored in these `ArrayList` structures is exactly $n$. Pre-sizing the map to `n` minimizes internal array bucket resizing.
2. **BFS Queue (`q`):** The queue stores array indices waiting to be processed layer-by-layer. In the worst-case configuration, the queue can hold up to $n$ elements at once.
3. **Visited Array (`seen`):** An explicit `boolean[]` array tracking visited states of size $n$, contributing $\mathcal{O}(n)$ space.

Combining these factors, the auxiliary space complexity remains strictly bound to linear space, or $\mathcal{O}(n)$.
