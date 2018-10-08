#输入一棵二叉树，判断该二叉树是否是平衡二叉树。
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)


    def TreeDepth(self,pRoot):
        if pRoot is None:
            return 0
        nleft = self.TreeDepth(pRoot.left)
        nright = self.TreeDepth(pRoot.right)
        return max(nleft,nright)+1