class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 從下面往上逐一確認(最下面皆為0，因為最下面深度是0)
        # 直到找到左右節點深度差距超過1的節點，回傳結果
        def check(root):
            if root is None:
                return 0
            l = check(root.left)
            r = check(root.right)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return 1 + max(l, r)
        return check(root) != -1