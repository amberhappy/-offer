#我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
# 总共有多少种方法？
#一般的结论，如果用1*m的方块覆盖m*n区域，递推关系式为f(n) = f(n-1) + f(n-m)，(n > m)
class Solution:
    def rectCover(self,number):
        if number ==0:
            return  0
        if number ==1:
            return 1
        if number ==2:
            return 2
        else:
            a = 1
            b = 2
            for i in range(2,number):
                a ,b = b,a+b
            return b