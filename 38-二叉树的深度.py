#输入一棵二叉树，求该树的深度。
# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。


from collections import deque

class Solution:
    def TreeDepth(self,pRoot):
        if pRoot is None:
            return 0
        dq = deque()
        layer =1
        dq.append((pRoot,1))
        while dq:
            node,layer  = dq.popleft()
            deep = layer
            if node.left is not None:
                dq.append((node.left,layer+1))
            if node.right:
                dq.append((node.right,layer+1))
        return deep