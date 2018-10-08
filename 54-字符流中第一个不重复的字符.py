#如果当前字符流没有存在出现一次的字符，返回#字符

class Solution:
    def __init__(self):
        self.s = ''
        self.dict = {}
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.dict[i]==1:
                return i
        return "#"


    def Insert(self, char):
        self.s = self.s+char
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char]=1