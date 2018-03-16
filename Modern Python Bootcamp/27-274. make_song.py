def make_song(n, beverage):
    count = n
    while True:
        if count > 1:
            yield f"{count} bottles of {beverage} on the wall."
            count -= 1
        elif count == 1:
            yield f"Only 1 bottle of {beverage} left!"
            count -= 1
        elif count == 0:
            yield f"No more {beverage}!"
            count -= 1
        else:
            raise StopIteration


for i in make_song(10, "soda"):
    print(i)
