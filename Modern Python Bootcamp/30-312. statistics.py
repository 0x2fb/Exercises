def statistics(a):
    with open(a, 'r') as file:
        storage = file.readlines()
        return {
            'lines': len(storage),
            'words': sum(len(line.split(" ")) for line in storage),
            'characters': sum(len(line) for line in storage)
        }
