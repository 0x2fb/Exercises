def find_and_replace(a, old, new):
    with open(a, "r") as file:
        text = file.read()
        new_text = text.replace(old, new)
    with open(a, "w") as file:
        file.write(new_text)
