class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        # dia 是樹的深度
        def dia(root):
            # 定義 nonlocal ans 是讓ans設為非local的變數，只影響函數內的範圍
            nonlocal ans
            if not root:
                return 0
            left=dia(root.left)
            right=dia(root.right)
            ans=max(ans,left+right) # 真正要回傳的是左右子樹的深度和
            return 1+max(right,left) # dia 回傳當前子樹深度
        dia(root)
        return ans