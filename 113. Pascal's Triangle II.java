import java.util.*;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        long val = 1;
        for (int i = 0; i <= rowIndex; i++) {
            row.add((int) val);
            val = val * (rowIndex - i) / (i + 1);
        }
        return row;
    }
    public static void main(String[] args) {
        Solution value = new Solution();
        System.out.println(value.getRow(3));
        System.out.println(value.getRow(0));
        System.out.println(value.getRow(1));
    }
}
