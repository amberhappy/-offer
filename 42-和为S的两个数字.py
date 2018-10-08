#输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
# 如果有多对数字的和等于S，输出两个数的乘积最小的。
from collections import Counter
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        for i in array:
            if tsum-i in array:
                if i!=tsum-i:
                    return (i,tsum-i)

        return []

