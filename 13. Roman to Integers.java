public class Solution {
    public int romanToInt(String s) {
        int total = 0;
        int lastValue = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int currentValue = getValue(s.charAt(i));
            total += currentValue < lastValue ? -currentValue : currentValue;
            lastValue = currentValue;
        }

        return total;
    }

    private int getValue(char roman) {
        switch (roman) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: throw new IllegalArgumentException("Invalid Roman numeral: " + roman);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.romanToInt("III"));      // Output: 3
        System.out.println(solution.romanToInt("LVIII"));    // Output: 58
        System.out.println(solution.romanToInt("MCMXCIV"));  // Output: 1994
    }
}
