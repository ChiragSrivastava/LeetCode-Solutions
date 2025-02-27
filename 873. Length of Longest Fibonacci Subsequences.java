import java.util.HashMap;

class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        int n = arr.length;
        HashMap<Integer, Integer> indexMap = new HashMap<>();
        HashMap<Integer, Integer> dp = new HashMap<>();
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            indexMap.put(arr[i], i);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int a = arr[j], b = arr[i];
                int c = a + b;
                if (indexMap.containsKey(c)) {
                    int k = indexMap.get(c);
                    int key = j * n + i;
                    int prevKey = (i * n) + k;
                    dp.put(prevKey, dp.getOrDefault(key, 2) + 1);
                    maxLen = Math.max(maxLen, dp.get(prevKey));
                }
            }
        }
        return maxLen >= 3 ? maxLen : 0;
    }
}
