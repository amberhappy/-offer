#请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
class Solution:

    def replaceSpace(self,a):

        s = list(a)
        length =  len(s)
        i = 0
        while i<length:
            if s[i] ==  ' ':
                s[i] = '%20'
            i += 1
        return ''.join(s)

# solution = Solution()
# a = 'I wanna be a superman'
# s = solution.replaceSpace(a)
# print(s)