class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return numbers
        new_list = [i for i in numbers ]
        new_list.sort()
        if len(new_list)==1:
            return True
        n = 0
        for j in range(len(new_list)-1):
            if new_list[j+1]>new_list[j]:
                n = n+ new_list[j+1]-new_list[j]
            else:
                return True
        if n<=4:
            return True
        else:
            return False