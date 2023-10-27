class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        # checks that current node value isn't None
        if ( not p is None ) and ( not q is None ):
            if not p.val == q.val:
                return False

            if not self.isSameTree(p.left, q.left):
                return False
            
            if not self.isSameTree(p.right, q.right):
                return False
            
            return True
        else:
            # checks that they both are None
            if type(p) == type(q):
                return True
            else:
                return False


sol = Solution()

ptest1 = TreeNode(1, TreeNode(2), TreeNode(3))
ptest2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(sol.isSameTree(ptest1,ptest2))

ptest1 = TreeNode(1, TreeNode(2))
ptest2 = TreeNode(1, None, TreeNode(2))
print(sol.isSameTree(ptest1,ptest2))