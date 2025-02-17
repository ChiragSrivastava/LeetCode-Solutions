class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2):
        def get_leaf_sequence(node):
            if not node:
                return []
            if not node.left and not node.right: 
                return [node.val]
            return get_leaf_sequence(node.left) + get_leaf_sequence(node.right)
        leaf_seq1 = get_leaf_sequence(root1)
        leaf_seq2 = get_leaf_sequence(root2)
        return leaf_seq1 == leaf_seq2
