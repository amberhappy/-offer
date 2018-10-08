#现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
class Solution:
    def Fibonacci(self,n):
        if n ==0:
            return 0
        if n == 1 :
            return 1
        if n ==2 :
            return 1
        if n >2:
            s = []*n
            s.append(1)
            s.append(1)
            for i in range(2, n):
                s.append(s[i - 2] + s[i - 1])
            return s[n - 1]


