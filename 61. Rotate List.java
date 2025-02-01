class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
    }

    public static ListNode deserialize(String s) {
        if (s == null || s.trim().isEmpty() || s.equals("[]")) {
            return null;
        }

        s = s.replaceAll("[\\[\\]]", "").trim();
        if (s.isEmpty()) {
            return null;
        }

        String[] values = s.split(",");
        ListNode head = new ListNode(Integer.parseInt(values[0].trim()));
        ListNode current = head;

        for (int i = 1; i < values.length; i++) {
            if (!values[i].trim().isEmpty()) {
                current.next = new ListNode(Integer.parseInt(values[i].trim()));
                current = current.next;
            }
        }

        return head;
    }

    public static String serialize(ListNode head) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");

        ListNode current = head;
        while (current != null) {
            sb.append(current.val);
            if (current.next != null) {
                sb.append(",");
            }
            current = current.next;
        }

        sb.append("]");
        return sb.toString();
    }
}

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }
        
        ListNode tail = head;
        int length = 1;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }
        
        tail.next = head;
        
        k %= length;
        if (k == 0) {
            tail.next = null;
            return head;
        }
        
        int stepsToNewTail = length - k;
        ListNode newTail = head;
        for (int i = 1; i < stepsToNewTail; i++) {
            newTail = newTail.next;
        }
        
        ListNode newHead = newTail.next;
        newTail.next = null;
        
        return newHead;
    }
}

public class Driver {
    public static void main(String[] args) {
        String input = "[1,2,3,4,5]";
        ListNode head = ListNode.deserialize(input);
        
        Solution solution = new Solution();
        ListNode result = solution.rotateRight(head, 2);
        
        System.out.println(ListNode.serialize(result));
    }
}
