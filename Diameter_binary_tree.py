def diameterOfBinaryTree(self, root):
    diameter = 0

    def dfs(root):
        nonlocal diameter
        if not root: return 0
        left = dfs(root.left)
        right = dfs(root.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1

    dfs(root)
    return diameter