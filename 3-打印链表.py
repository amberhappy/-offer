#输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def printListFromTailToHead(self,listNode):
        l = []
        head = listNode
        while head:
            l.insert(0,head.val)
            head = head.next
        return l
