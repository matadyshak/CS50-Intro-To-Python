import random

class Hat:
    houses = ["Grif", "Huff", "Raven", "Sly"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")