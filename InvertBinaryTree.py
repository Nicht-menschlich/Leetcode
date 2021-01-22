#https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def swapNodes(self, left: TreeNode, right: TreeNode):
        if left is not None:
            left.left, left.right = self.swapNodes(left.left, left.right)
        if right is not None:
            right.left, right.right = self.swapNodes(right.left, right.right)
        between = left
        left = right
        right = between
        return left, right

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = self.swapNodes(root.left, root.right)
            return root