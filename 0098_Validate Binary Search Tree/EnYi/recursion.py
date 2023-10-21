class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursion
        def check(root, min_val, max_val):
            if root is None:
                return True
            if (min_val is not None and root.val <= min_val) or (max_val is not None and root.val >= max_val):
                return False
            # 如果符合條件，左子樹 max_val 替換為 root.val，右子樹替換為 min_val
            return check(root.left, min_val, root.val) and check(root.right, root.val, max_val)
        return check(root, None, None)