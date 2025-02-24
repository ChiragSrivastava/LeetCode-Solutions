import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
class Solution {
    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        return buildTree(preorder, postorder, new int[]{0}, new int[]{0});
    }

    private TreeNode buildTree(int[] preorder, int[] postorder, int[] preIndex, int[] postIndex) {
        TreeNode root = new TreeNode(preorder[preIndex[0]++]);
        if (root.val == postorder[postIndex[0]]) {
            postIndex[0]++;
            return root;
        }
        if (preIndex[0] < preorder.length) {
            root.left = buildTree(preorder, postorder, preIndex, postIndex);
        }
        if (preIndex[0] < preorder.length && postorder[postIndex[0]] != root.val) {
            root.right = buildTree(preorder, postorder, preIndex, postIndex);
        }
        postIndex[0]++;    
        return root;
    }
}
