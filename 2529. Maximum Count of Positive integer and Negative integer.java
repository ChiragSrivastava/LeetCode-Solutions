import java.util.Arrays;

class Solution {
    public int maximumCount(int[] nums) {
        int n = nums.length;
        int firstPositive = lowerBound(nums, 0);
        int firstZero = lowerBound(nums, 1);
        int negativeCount = firstPositive;
        int positiveCount = n - firstZero;        
        return Math.max(negativeCount, positiveCount);
    }
    private int lowerBound(int[] nums, int target) {
        int left = 0, right = nums.length;        
        while (left < right) {
            int mid = left + (right - left) / 2;            
            if (nums[mid] >= target) right = mid;
            else left = mid + 1;
        }        
        return left;
    }
}
