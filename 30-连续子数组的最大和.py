#给一个数组，返回它的最大连续子序列的和
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        max_sum,cur_sum = -0xffffffff,0
        for i in array:
            if cur_sum<0:
                cur_sum = i
            else:
                cur_sum = cur_sum+i

            if cur_sum>max_sum:
                max_sum = cur_sum
        return max_sum