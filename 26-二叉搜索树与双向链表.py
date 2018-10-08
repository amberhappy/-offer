#输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向

#思路：   先中序遍历，将所有的节点保存到一个列表中。对这个list[:-1]进行遍历，
#         每个节点的right设为下一个节点，下一个节点的left设为上一个节点

class Solution:
    def Convert(self,pRootOFTree):
        if not pRootOFTree:
            return
        self.arr = []
        self.midTraveral(pRootOFTree)

        for i,v in enumerate(self.arr[:-1]):
            v.right = self.arr[i+1]
            self.arr[i+1].left =v
        return self.arr[0]


    def midTraveral(self,root):
        if not root:
            return
        self.midTraveral(root.left)
        self.arr.append(root)
        self.midTraveral(root.right)


def preTraverse(root):
    '''
    前序遍历
    '''
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def midTraverse(root):
    '''
    中序遍历
    '''
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


def afterTraverse(root):
    '''
    后序遍历
    '''
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

 def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)