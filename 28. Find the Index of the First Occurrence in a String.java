class Solution {
    public int strStr(String hs, String needle) {
        int hayLen = hs.length();
        int needleLen = needle.length();
        
        if (needleLen == 0) return 0;
        if (needleLen > hayLen) return -1;

        for (int i = 0; i <= hayLen - needleLen; i++) {
            if (hs.substring(i, i + needleLen).equals(needle)) {
                return i;
            }
        }        
        return -1;
    }
}
