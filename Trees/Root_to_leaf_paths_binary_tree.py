#1. Idea here is we want to return a list of strings which contains all of the root to leaf paths in the binary tree.
#2. So initialize a list (path_list) then we are going to make a recursive call function. In the function we will pass the root of the binary tree and a empty string which we will modify and add node values as we recurse.
#3. If the root is NOT none, we want to add that node value to our string, this will always begin from the ROOT of the binary tree. This will build our string of paths.
#4. Once we come accross a leaf our second condition will be met thus we know that if we hit a leaf we have reached the END of the path, so we have our root to leaf path, hence we should add that path to our path_list, not path_list will be global for inner function.
#5. Otherwise if we are not at a leaf, we still want to build our list and add the node value BUT we want to keep recursing down the tree until we hit the leaves, so we simply recurse left and right respectivley.
#6. Rememeber to pass the path + -> as this will build the string according to the desired output. Done!
def binaryTreePaths(self, root):
    path_list = []
    def recurse(root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                path_list.append(path)
            else:
                recurse(root.left, path + "->")
                recurse(root.right, path + "->")
    recurse(root, "")
    return path_list