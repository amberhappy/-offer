#给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
class Solution:
    def multiply(self,A):
        count = len(A)
        B = [1]*count
        for i in range(len(A)):
            b = 1
            for j in range(len(A)):
                if i ==j:
                    continue
                b = b*A[j]
            B[i] = b
        return B


