def mode(ls):
    ndict = {n: ls.count(n) for n in ls}
    max_num = max(ndict.keys())
    for k, v in ndict.items():
        if v == max_num:
            return k


print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))  # 4)
