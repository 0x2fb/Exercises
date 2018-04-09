def show_magicians(ls):
    for m in ls:
        print(m)


def make_great(ls):
    return ["The Great " + i for i in ls]


magicians = ["Tom", "Lara", "Dorothy"]
new_magicians = make_great(magicians)
show_magicians(magicians)
show_magicians(new_magicians)
