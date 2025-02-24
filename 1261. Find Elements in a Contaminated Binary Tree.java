import java.util.HashSet;
import java.util.Set;

class FindElements {
    private Set<Integer> values = new HashSet<>();
    public FindElements(TreeNode root) {
        recoverTree(root, 0);
    }
    private void recoverTree(TreeNode node, int val) {
        if (node == null) return;
        node.val = val;
        values.add(val);
        recoverTree(node.left, 2 * val + 1);
        recoverTree(node.right, 2 * val + 2);
    }
    public boolean find(int target) {
        return values.contains(target);
    }
}
