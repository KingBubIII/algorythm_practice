class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.inorder = []
    def inorderTraversal(self, root) -> list[int]:
        temp = []
        if root is None:
            return temp
        if not root.left is None:
            temp.extend(self.inorderTraversal(root.left))
        if not root.val is None or not root is None:
            temp.append(root.val)

        if not root.right is None:
            temp.extend(self.inorderTraversal(root.right))
        
        return temp

mytree = TreeNode(1, None, TreeNode(2,TreeNode(3),None))
mytree2 = TreeNode(None)
test = Solution()

print(test.inorderTraversal(root=mytree))
print(test.inorderTraversal(root=mytree2))