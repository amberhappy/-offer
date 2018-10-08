#在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

#归并排序思想

class Solution:
    def InversePairs(self,data):
        return self.inverseCount(data[:],0,len(data)-1,data[:])%1000000007

    def inverseCount(self,tmp,start,end,data):
        if end -start <1:
            return 0
        if end-start ==1:
            if data[start]<=data[end]:
                return 0
            else:
                tmp[start],tmp[end] = data[end],data[start]
                return 1

        mid = (start+end)//2
        cnt = self.inverseCount(data,start,mid,tmp)+self.inverseCount(data,mid+1,end,tmp)

        i =start
        j = mid +1
        ind = start

        while i<=mid and j <=end:
            if data[i]<=data[j]:
                tmp[ind] = data[i]
                i+=1
            else:
                tmp[ind]= data[j]
                cnt+=mid-i+1
                j+=1
            ind +=1
        while i<=mid:
            tmp[ind] = data[i]
            i+=1
            ind+=1
        while j<=end:
            tmp[ind] = data[j]
            j+=1
            ind +=1
        return cnt