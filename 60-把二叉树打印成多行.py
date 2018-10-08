class Solution:
    def Print(self,pRoot):

        if not pRoot:
            return []
        res = []
        tmp = [pRoot]
        while tmp:
            size = len(tmp)
            row = []
            for i in tmp:
                row.append(i.val)
            res.append(row)
            for i in range(size):
                node = tmp.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
        return res