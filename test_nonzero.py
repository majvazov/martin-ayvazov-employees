class Person:
    def __init__(self, weight, hight):
        self.weight = weight
        self.hight = hight

    def __nonzero__(self):
        return bool(self.weight or self.hight)

p = Person(23,23)
