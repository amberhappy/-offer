def bubble(List):
    length = len(List)
    for i in range (0,length):
        for j in range(i+1,length):
            if List[i]>List[j]:
                List[i],List[j] = List[j],List[i]
    return List

# a = [4,8,7,3,2]
# m = bubble(a)
# print(m)
