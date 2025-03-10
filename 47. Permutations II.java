import java.util.*;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        boolean[] used = new boolean[nums.length];
        backtrack(nums, new ArrayList<>(), used, result);
        return result;
    }
    private void backtrack(int[] nums, List<Integer> temp, boolean[] used, List<List<Integer>> result) {
        if (temp.size() == nums.length) {
            result.add(new ArrayList<>(temp));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            temp.add(nums[i]);
            backtrack(nums, temp, used, result);
            temp.remove(temp.size() - 1);
            used[i] = false;
        }
    }
    public static void main(String[] args) {
        Solution value = new Solution();
        System.out.println(value.permuteUnique(new int[]{1,1,2}));
        System.out.println(value.permuteUnique(new int[]{1,2,3}));
    }
}
