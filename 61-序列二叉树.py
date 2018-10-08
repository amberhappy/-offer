#请实现两个函数，分别用来序列化和反序列化二叉树

class Solution:
    flag = -1
    def Serialize(self, root):
        s =""
        s = self.recursion(root,s)
        return s

    def recursion(self,root,s):
        if root is None:
            s = '#,'
            return s
        s = str(root.val)+","
        left = self.recursion(root.left,s)
        right = self.recursion(root.right,s)
        s +=left+right
        return s

    def deser(self,s):
        self.flag +=1
        l = s.split(",")
        if self.flag >len(s):
            return None
        root = None
        if (l[self.flag]!='#'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.deser(s)
            root.right = self.deser(s)
        return root
