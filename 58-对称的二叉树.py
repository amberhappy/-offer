#请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
class Solution:
    def isSymmetrical(self, pRoot):
        return self.issymm(pRoot,pRoot)

    def issymm(self,proot1,proot2):
        if not proot1 and not proot2:
            return True
        if not proot1 or not proot2:
            return False
        if proot1.val!=proot2.val:
            return False
        return self.issymm(proot1.left,proot2.right) and self.issymm(proot1.right,proot2.left)