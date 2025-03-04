class Person:
    def __init__(self, name, health, armor, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon

class Knight(Person):
    def __init__(self, name, health, armor, weapon):
        super().__init__(name, health, armor, weapon)
    def hit(self,enemy):
        if (enemy.armor - self.weapon.power) < 0:
            damage = (enemy.armor + enemy.health) - self.weapon.power
        else:
            damage = 0
        if self.weapon.power >= enemy.armor:
            enemy.armor = 0
        print(f'{self.name} атакует {enemy.name} с оружием {self.weapon.name} \n {enemy.name} получает {damage} урона! Осталось здоровья: {enemy.health - damage}, брони: {enemy.armor}'
            )
