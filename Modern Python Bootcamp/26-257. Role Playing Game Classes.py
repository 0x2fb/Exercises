class Character(object):

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):

    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        print(f"{self.name}: I heard monsters running around last night!")


villager = NPC('Bob', 10, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
villager.speak()
