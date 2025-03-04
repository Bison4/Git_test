class Weapon:
    def __init__(self,name, power):
        self.name = name
        self.power = power


class Sword(Weapon):
    def __init__(self, name, power):
        super().__init__( name, power)
