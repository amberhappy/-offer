class Solution:
    def ReverseSentence(self, s):
        s_split = s.split(" ")
        s_reverse = s_split[::-1]
        return " ".join(s_reverse)

# a = "i am a student"
# aa = a.split(" ")
# print(aa[::-1])
# print(" ".join(aa[::-1]))