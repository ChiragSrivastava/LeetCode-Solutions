public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        
        String s = Integer.toString(x);
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        System.out.println(solution.isPalindrome(121));  // true
        System.out.println(solution.isPalindrome(-121)); // false
        System.out.println(solution.isPalindrome(10));   // false
    }
}
