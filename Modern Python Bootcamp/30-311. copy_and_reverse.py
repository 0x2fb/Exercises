def copy_and_reverse(a, b):
    with open(a, 'r') as file:
        storage = file.read()
    with open(b, 'w') as copyfile:
        copyfile.write(storage[::-1])
