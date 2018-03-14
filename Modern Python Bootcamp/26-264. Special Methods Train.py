class Train:
    def __init__(self, num):
        self.num_cars = num

    def __repr__(self):
        return f'{self.num_cars} car train'

    def __len__(self):
        return self.num_cars


d = Train(4)
print(d)
print(len(d))
