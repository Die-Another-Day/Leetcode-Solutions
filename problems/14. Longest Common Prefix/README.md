# Longest Common Prefix

![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)
![Java](https://img.shields.io/badge/language-Java-007396?style=for-the-badge&logo=java&logoColor=white)

## 📌 Problem Description

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

### Examples

**Example 1:**
- **Input:** `strs = ["flower","flow","flight"]`
- **Output:** `"fl"`

**Example 2:**
- **Input:** `strs = ["dog","racecar","car"]`
- **Output:** `""`
- **Explanation:** There is no common prefix among the input strings.

### Constraints
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

---

## 🚀 Solution Approach: Horizontal Scanning

This solution uses the **Horizontal Scanning** technique. 

1. **Initialization:** Assume the first string in the array is the initial `prefix`.
2. **Comparison:** Iterate through the rest of the strings in the array.
3. **Trimming:** For each string, check if the current `prefix` exists at the start (index 0). If it doesn't, shorten the `prefix` by one character from the end using `substring(0, length - 1)` and check again.
4. **Early Exit:** If at any point the `prefix` becomes empty, return `""` immediately as no common prefix can exist.

### Code Snippet
```java
public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";
    
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) != 0) {
            prefix = prefix.substring(0, prefix.length() - 1);
            if (prefix.isEmpty()) return "";
        }
    }
    return prefix;
}
