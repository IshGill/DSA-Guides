def countNodes(self, root):
    self.count = 0
    def preOrder(root):
        if not root:
            return None
        else:
            self.count += 1
            preOrder(root.left)
            preOrder(root.right)

    preOrder(root)
    return self.count
