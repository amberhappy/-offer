#给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
class Solution:
    def EntryNodeOfLoop(self, pHead):
        tmp =[]
        head = pHead
        while head:
            if head in tmp:
                return head
            else:
                tmp.append(head)
            head= head.next