#请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
#约瑟夫环问题

# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2,n+1):
            last = (last + m)%i
        return last