#把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<1:
            return 0
        uglyList = [1]
        indexTwo = 0
        indexTree = 0
        indextFive =0

        for i in range(index-1):
            newUgly = min(uglyList[indexTwo]*2,uglyList[indexTree]*3,uglyList[indextFive]*5)
            uglyList.append(newUgly)
            if newUgly%2==0:
                indexTwo+=1
            if newUgly%3 ==0:
                indexTree+=1
            if newUgly%5 == 0:
                indextFive+=1
        return uglyList[-1]