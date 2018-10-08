#在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
# 并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
import sys
import collections
class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == "":
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
                break


#
# s ="aaaab"
# s = list(s)
# tmp = collections.Counter(s)
# for v,m in tmp.items():
#     print(v)
#     print(m)

