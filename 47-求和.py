#求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
class Solution:
    # def Sum_Solution(self, n):
    #     return sum(list(range(1,n+1)))

    def __init__(self):
        self.sum = 0
    def sum_solution(self,n):
        def summary(n):
            self.sum +=n
            n = n-1
            return n>0 and self.sum_solution(n)
        summary(n)
        return self.sum