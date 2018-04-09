def show_magicians(ls):
    for m in ls:
        print(m)


def make_great(ls):
    return ["The Great " + i for i in ls]


magicians = ["Tom", "Lara", "Dorothy"]
show_magicians(make_great(magicians))
