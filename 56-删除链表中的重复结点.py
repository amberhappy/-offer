#在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
#  例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
class Solution:
    def deleteDuplication(self, pHead):

        # 如果链表为空或者只有一个元素，直接返回
        if not pHead or not pHead.next:     ## 结点重复，继续查找后面是否还有重复
            return pHead
        if pHead.val ==pHead.next.val:       # 当前第一个重复结点为pHead
            p = pHead.next.next
            while p and p.val is pHead.val:  # 递归处理剩余结点
                p = p.next
            return self.deleteDuplication(p)
        pHead.next = self.deleteDuplication(pHead.next)
        return pHead
