class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(self.name, "is attacking!")

    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.name, "took", damage, "damage.")
        print("Remaining health:", self.health)

player1 = Character("Neon", 100)

player1.attack()
player1.take_damage(30)
