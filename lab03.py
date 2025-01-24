# Dice options using list() and range()
diceOptions = list (range(1, 7))

# Weapons Array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Display available weapons
print("Available weapons: ", ', '.join(weapons))

def get_combat_strenght(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Invalid input! Please enter a number between 1-6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1-6")

combatStrength = get_combat_strenght("Enter your combat strength (1-6): ")
mCombatStrength = get_combat_strenght("Enter monster's combat strength (1-6): ")