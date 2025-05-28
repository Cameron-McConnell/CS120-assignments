import tbc

def main():
    # Create hero character
    hero = tbc.Character()
    hero.name = "Dark Knight"
    hero.hitPoints = 12
    hero.hitChance = 70
    hero.maxDamage = 6
    hero.armor = 3

    # Create monster character (using constructor parameters)
    monster = tbc.Character("Dragon", 25, 50, 8, 2)

    # Show stats
    hero.printStats()
    monster.printStats()

    # Start combat
    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()