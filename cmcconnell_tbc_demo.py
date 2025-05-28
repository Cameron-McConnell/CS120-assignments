import random

class Character:
    def __init__(self, name="Unknown", hit_points=1, hit_chance=50, max_damage=1, armor=0):
        self.name = name
        self.hit_points = hit_points
        self.hit_chance = hit_chance
        self.max_damage = max_damage
        self.armor = armor

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value) if value else "Unknown"

    @property
    def hit_points(self):
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value):
        self._hit_points = self._validate_integer(value, default=1)

    @property
    def hit_chance(self):
        return self._hit_chance

    @hit_chance.setter
    def hit_chance(self, value):
        self._hit_chance = self._validate_integer(value, min=0, max=100, default=50)

    @property
    def max_damage(self):
        return self._max_damage

    @max_damage.setter
    def max_damage(self, value):
        self._max_damage = self._validate_integer(value, min=1, default=1)

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value):
        self._armor = self._validate_integer(value, min=0, default=0)

    def _validate_integer(self, value, min=-float('inf'), max=float('inf'), default=0):
        """Validates and clamps integer values"""
        try:
            value = int(value)
            if value < min:
                print(f"Warning: Value {value} too small. Using {min}.")
                return min
            elif value > max:
                print(f"Warning: Value {value} too large. Using {max}.")
                return max
            return value
        except (ValueError, TypeError):
            print(f"Warning: {value} must be an integer. Using default {default}.")
            return default

    def print_stats(self):
        """Prints character statistics"""
        print("==================")
        print(f"NAME: {self.name}")
        print("------------------")
        print(f"Hit Points: {self.hit_points}")
        print(f"Hit Chance: {self.hit_chance}%")
        print(f"Max Damage: {self.max_damage}")
        print(f"Armor:      {self.armor}")
        print("==================")

    def attack(self, target):
        """Performs an attack on target character"""
        messages = []
        attack_roll = random.randint(1, 100)
        
        if attack_roll <= self.hit_chance:
            base_damage = random.randint(1, self.max_damage)
            actual_damage = max(0, base_damage - target.armor)
            target.hit_points -= actual_damage
            
            messages.append(f"{self.name} hits {target.name}!")
            messages.append(f"  Damage dealt: {actual_damage} (after armor)")
        else:
            messages.append(f"{self.name} missed {target.name}!")
        
        return messages


def start_battle(character1, character2):
    """Manages the turn-based combat between two characters"""
    print(f"BATTLE STARTED: {character1.name} vs {character2.name}\n")
    
    # Show initial stats
    character1.print_stats()
    character2.print_stats()
    print("\n")
    
    # Battle loop
    while character1.hit_points > 0 and character2.hit_points > 0:
        # Character 1's turn
        print(f"--- {character1.name}'s turn ---")
        for message in character1.attack(character2):
            print(message)
        
        # Check if character2 is defeated
        if character2.hit_points <= 0:
            break
        
        # Character 2's turn
        print(f"\n--- {character2.name}'s turn ---")
        for message in character2.attack(character1):
            print(message)
        
        # Display current HP
        print("\nCURRENT STATUS:")
        print(f"{character1.name} HP: {character1.hit_points}")
        print(f"{character2.name} HP: {character2.hit_points}")
        
        # Pause between rounds
        input("\nPress ENTER to continue...\n")
    
    # Determine winner
    print("\n=======================")
    if character1.hit_points > 0:
        print(f"{character1.name} WINS THE BATTLE!")
    else:
        print(f"{character2.name} WINS THE BATTLE!")
    print("=======================")


def demo():
    """Demonstrates the combat system with sample characters"""
    # Create hero character
    hero = Character()
    hero.name = "Dark Knight"
    hero.hit_points = 10
    hero.hit_chance = 50  # Typo fixed to hit_chance
    hero.max_damage = 5
    hero.armor = 2
    
    # Create monster character
    monster = Character("Dragon", 20, 30, 5, 0)
    
    # Start battle
    start_battle(hero, monster)


if __name__ == "__main__":
    demo()