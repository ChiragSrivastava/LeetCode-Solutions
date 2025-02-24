import java.util.*;

class Solution {
    public int mostProfitablePath(int[][] edges, int bob, int[] amount) {
        int n = amount.length;
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; i++) tree[i] = new ArrayList<>();
        for (int[] edge : edges) {
            tree[edge[0]].add(edge[1]);
            tree[edge[1]].add(edge[0]);
        }
        Map<Integer, Integer> bobTime = new HashMap<>();
        findBobPath(bob, -1, 0, tree, bobTime);
        return dfsAlice(0, -1, 0, tree, bobTime, amount);
    }
    private boolean findBobPath(int node, int parent, int time, List<Integer>[] tree, Map<Integer, Integer> bobTime) {
        bobTime.put(node, time);
        if (node == 0) return true;
        for (int neighbor : tree[node]) {
            if (neighbor == parent) continue;
            if (findBobPath(neighbor, node, time + 1, tree, bobTime)) return true;
        }
        bobTime.remove(node);
        return false;
    }
    private int dfsAlice(int node, int parent, int time, List<Integer>[] tree, Map<Integer, Integer> bobTime, int[] amount) {
        if (bobTime.containsKey(node)) {
            int bobArrival = bobTime.get(node);
            if (time < bobArrival) {
            } else if (time == bobArrival) {
                amount[node] /= 2;
            } else {
                amount[node] = 0;
            }
        }
        int maxIncome = Integer.MIN_VALUE;
        boolean isLeaf = true;
        for (int neighbor : tree[node]) {
            if (neighbor == parent) continue;
            isLeaf = false;
            maxIncome = Math.max(maxIncome, dfsAlice(neighbor, node, time + 1, tree, bobTime, amount));
        }
        return amount[node] + (isLeaf ? 0 : maxIncome);
    }
}
