class Player:
    def blast(self, enemy):
        print("The Player blasts an enemy.\n")
        enemy.die()

class Alien:
    def die(self):
        print("The alien gasps and says. 'Oh, this is it. This is the big one.")
        print("Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...")
        print("Good-bye, cruel universe.\n\n")

print("\t\tDeath of an Alien\n")
hero = Player()
invader = Alien()
hero.blast(invader)
print("Press the enter key to exit.")
