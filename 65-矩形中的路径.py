#
class Solution:
    def hasPath(self,matrix,rows,cols,path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j]==path[0]:
                    if self.find(list(matrix),rows,cols,path[1:],i,j):
                        return True
        return False
    def find(self,matirx,rows,cols,path,i,j):
        if not path:
            return True
        matirx[i * cols + j] = '0'

        if j+1<cols and matirx[i*cols+j+1]==path[0]:
            return self.find(matirx,rows,cols,path[1:],i,j+1)
        if j-1>=0 and matirx[i*cols+j-1]==path[0]:
            return self.find(matirx,rows,cols,path[1:],i,j-1)
        if i+1<rows and matirx[(i+1)*cols+j]==path[0]:
            return self.find(matirx, rows, cols, path[1:], i + 1, j)
        elif i - 1 >= 0 and matirx[(i - 1) * cols + j] == path[0]:
            return self.find(matirx, rows, cols, path[1:], i - 1, j)
        else:
            return False