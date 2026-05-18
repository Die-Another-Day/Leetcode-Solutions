class Solution {
    public int minJumps(int[] arr) {
        int n = arr.length;
        if (n <= 1) return 0;
        Map<Integer, List<Integer>> graph = new HashMap<>(n);
        for (int i = 0; i < n; i++) {
            graph.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }
        Queue<Integer> q = new ArrayDeque<>();
        boolean[] seen = new boolean[n];
        
        q.offer(0);
        seen[0] = true;
        int steps = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0) {
                int i = q.poll();

                if (i == n - 1) return steps;
                List<Integer> sameValues = graph.get(arr[i]);
                if (sameValues != null) {
                    for (int nextIdx : sameValues) {
                        if (!seen[nextIdx]) {
                            seen[nextIdx] = true; 
                            q.offer(nextIdx);
                        }
                    }
                    graph.remove(arr[i]);
                }
                if (i + 1 < n && !seen[i + 1]) {
                    seen[i + 1] = true;
                    q.offer(i + 1);
                }
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
