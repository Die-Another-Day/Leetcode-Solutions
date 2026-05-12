# 🚀 LeetCode 1665: Minimum Initial Energy to Finish Tasks

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)
![Topic: Greedy](https://img.shields.io/badge/Topic-Greedy-blue)
![Topic: Sorting](https://img.shields.io/badge/Topic-Sorting-orange)

## 📝 Problem Description

You are given an array `tasks` where `tasks[i] = [actual_i, minimum_i]`:
* **actual_i**: The actual amount of energy you spend to finish the task.
* **minimum_i**: The minimum amount of energy you require to begin the task.

The goal is to find the **minimum initial amount of energy** you will need to finish all the tasks in any order.

---

## 💡 Approach: The Greedy Strategy

The problem is a classic greedy challenge. To minimize the starting energy, we need to pick the best sequence. 

### The Core Logic:
We should prioritize tasks where the "requirement gap" is the largest. The gap is defined as:
`minimum_i - actual_i`

By sorting tasks based on this difference in descending order (or `actual - minimum` in ascending order), we ensure that we tackle tasks with higher relative requirements while we still have the most energy available.

### Simulation Steps:
1. **Sort** the tasks by the difference `(actual - minimum)`.
2. **Iterate** through the sorted tasks.
3. If the `current_energy` is less than the `minimum` required for a task, we increase our `initial_energy` by the deficit and set our `current_energy` to that minimum.
4. **Subtract** the `actual` energy spent from our `current_energy`.

---

## 💻 Implementation

```java
class Solution {
    public int minimumEffort(int[][] tasks) {
        // Sort tasks based on the difference (actual - minimum)
        // This prioritizes tasks that require more "buffer" energy first
        Arrays.sort(tasks, (a, b) -> (a[0] - a[1]) - (b[0] - b[1]));
        
        int totalInitialEnergy = 0;
        int currentEnergy = 0;
        
        for (int[] task : tasks) {
            int actual = task[0];
            int minimum = task[1];
            
            // If current energy is less than required minimum, we need to add more
            if (currentEnergy < minimum) {
                totalInitialEnergy += (minimum - currentEnergy);
                currentEnergy = minimum;
            }
            
            // After starting, subtract the actual energy spent
            currentEnergy -= actual;
        }
        
        return totalInitialEnergy;
    }
}
