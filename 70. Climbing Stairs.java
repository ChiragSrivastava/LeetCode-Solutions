public class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;

        int oneStepBefore = 2;
        int twoStepsBefore = 1;
        int allWays = 0;

        for (int i = 3; i <= n; i++) {
            allWays = oneStepBefore + twoStepsBefore;
            twoStepsBefore = oneStepBefore;
            oneStepBefore = allWays;
        }

        return allWays;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.climbStairs(2)); 
        System.out.println(solution.climbStairs(3)); 
        System.out.println(solution.climbStairs(5)); 
    }
}
