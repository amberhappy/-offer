#定义栈的数据结构，
# 请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））
#思路：利用一个辅助栈来存放最小值
#
#     栈  3，4，2，5，1
#     辅助栈 3，3，2，2，1
# 每入栈一次，就与辅助栈顶比较大小，如果小就入栈，如果大就入栈当前的辅助栈顶
# 当出栈时，辅助栈也要出栈
# 这种做法可以保证辅助栈顶一定都当前栈的最小值
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []
    def push(self, node):
        min =self.min()
        if not min or node<min:
            self.assist.append(node)
        else:
            self.assist.append(min)
        self.stack.append(node)

    def pop(self):
        if self.stack:
            self.assist.pop()
            return self.stack.pop()
    def top(self):
        if self.stack():
            return self.stack[-1]
    def min(self):
        if self.assist:
            return self.assist[-1]