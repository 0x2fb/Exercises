def list_check(list_input):
    return all(type(i) == list for i in list_input)
