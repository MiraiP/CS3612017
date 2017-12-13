a = [[1,3],[3,6]]


def big_list(l):
    large_list = []
    if type(l) is list:
        for i in l:
            for x in i:
                large_list.append(x)
        return large_list

print(big_list(a))
