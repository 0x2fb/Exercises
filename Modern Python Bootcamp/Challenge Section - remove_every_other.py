def remove_every_other(lst):
    # rm_lst = []
    # for i, k in enumerate(lst):
    #     if i % 2 == 0:
    #         rm_lst.append(k)
    # return rm_lst
    return [k for i, k in enumerate(lst) if i % 2 == 0]
