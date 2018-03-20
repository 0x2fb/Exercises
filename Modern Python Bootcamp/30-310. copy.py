def copy(a, b):
    with open(a, 'r') as file:
        storage = file.readlines()
    with open(b, 'w') as copyfile:
        copyfile.writelines(storage)
