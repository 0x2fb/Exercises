def find_the_duplicate(ls):
    set_ls = set(ls)
    for i in set_ls:
        count = 0
        for j in ls:
            if i == j:
                count += 1
                if count > 1:
                    return i
    return None
