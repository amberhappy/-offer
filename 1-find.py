#在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:

    def find(self,target, array):

        row = len(array)-1
        col = len(array[0])-1

        i = row
        j = 0

        while i>=0 and j<=col:
            if target<array[i][j]:
                i -= 1
            elif target>array[i][j]:
                j += 1
            else:
                print(array[i][j])
                return True
        return False

# aa = Solution()
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# target =5
# aa.find(target ,array)

