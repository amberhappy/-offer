#有 n 个学生站成一排，每个学生有一个能力值，
# 牛牛想从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，
#  使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？

import sys
n = int(input("n sutudent:"))
arr = map(int,input().split())
K,D = map(int,input().split())

fm = [([0]*n) for i in range(K)]
fn = [([0]*n) for i in range(K)]

for i in range(n):
    fm[0][i]=arr[i]
    fn[0][i]= arr[i]

for i in range(n):
    for k in range(1,K):
        for j in range(i-1,max(0,i-D)-1,-1):
            fm[k][i] = max(fm[k][i], max(fm[k - 1][j] * arr[i], fn[k - 1][j] * arr[i]))
            fn[k][i] = min(fn[k][i], min(fm[k - 1][j] * arr[i], fn[k - 1][j] * arr[i]))
    res = max(res, fm[K - 1][i])
print(res)