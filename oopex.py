class Player(): 
    def __init__(self, strengthInput, nameInput):
        #this is where we define the attributes of a player
        self.health = 100
        self.strength = strengthInput
        self.name = nameInput

    def workout(self):
        print(f"{self.name} is working hard to improve." )
        self.strength += 5
        return self

    def attack(self, otherPlayer):
        otherPlayer.health -= self.strength
        return self

    def displayInfo(self):
        print(f"{self.name}'s health: {self.health}. Strength: {self.strength}")
        return self


#anything created using a class (blueprint) is called an object. These are player objects
player1 = Player(10, "Joe")
player2 = Player(10, "Junior")
player3 = Player(10, "Rex")

print("***********")

player1.workout().workout().workout()

player2.workout().workout()

player3.attack(player1).attack(player2)

player1.displayInfo()
player2.displayInfo()
player3.displayInfo()
