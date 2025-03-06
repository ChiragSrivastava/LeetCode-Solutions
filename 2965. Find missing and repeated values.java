import java.util.*;

class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int size = n * n;
        int[] freq = new int[size + 1];        
        int repeated = -1, missing = -1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                freq[grid[i][j]]++;
            }
        }
        for (int num = 1; num <= size; num++) {
            if (freq[num] == 2) {
                repeated = num;
            } else if (freq[num] == 0) {
                missing = num;
            }
        }
        return new int[]{repeated, missing};
    }
    public static void main(String[] args) {
        Solution value = new Solution();
        int[][] grid1 = {{1, 3}, {2, 2}};
        System.out.println(Arrays.toString(value.findMissingAndRepeatedValues(grid1)));
        int[][] grid2 = {{9, 1, 7}, {8, 9, 2}, {3, 4, 6}};
        System.out.println(Arrays.toString(value.findMissingAndRepeatedValues(grid2)));
    }
}
