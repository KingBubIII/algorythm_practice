class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)

        if left_count > right_count or left_count == right_count:
            count = left_count+1
        elif right_count > left_count:
            count = right_count+1
        else:
            count = 1

        return count
    

sol = Solution()

test1 = TreeNode(3, TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(sol.maxDepth(test1))

test2 = TreeNode(1,TreeNode(None),TreeNode(2))
print(sol.maxDepth(test2))


