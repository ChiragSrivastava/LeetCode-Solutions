import java.util.*;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int index = 0;
        while (index < words.length) {
            int totalChars = words[index].length();
            int last = index + 1;
            while (last < words.length && totalChars + 1 + words[last].length() <= maxWidth) {
                totalChars += 1 + words[last].length();
                last++;
            }
            int numWords = last - index;
            int numSpaces = maxWidth - totalChars + (numWords - 1);
            StringBuilder line = new StringBuilder();
            if (last == words.length || numWords == 1) {
                for (int i = index; i < last; i++) {
                    line.append(words[i]);
                    if (i < last - 1) line.append(" ");
                }
                while (line.length() < maxWidth) line.append(" ");
            } 
            else {
                int spaceSlots = numWords - 1;
                int extraSpaces = numSpaces % spaceSlots;
                int spacesPerSlot = numSpaces / spaceSlots;
                
                for (int i = index; i < last; i++) {
                    line.append(words[i]);
                    if (i < last - 1) {
                        int spaces = spacesPerSlot + (i - index < extraSpaces ? 1 : 0);
                        for (int j = 0; j < spaces; j++) line.append(" ");
                    }
                }
            }
            result.add(line.toString());
            index = last;
        }
        return result;
    }
}
