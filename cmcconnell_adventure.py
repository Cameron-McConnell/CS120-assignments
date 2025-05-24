def main():
    """
    Main game loop that manages the game flow from start to quit
    """
    game_data = getGame()  # Get the multi-dimensional dictionary structure
    current_node = "start"  # Always begin at the start node
    
    while current_node != "quit":
        current_node = playNode(current_node, game_data)
    
    print("Thanks for playing!")

def getGame():
    """
    Returns the game data structure as a multi-dimensional dictionary
    Each node contains: description, menuA, nodeA, menuB, nodeB
    """
    return {
        "start": (
            "You are on a boat. It's on fire",
            "Stay on the boat", "stay",
            "Jump in the water", "water"
        ),
        "stay": (
            "Did I mention the boat was ON FIRE?",
            "Start over", "start",
            "Quit", "quit"
        ),
        "water": (
            "You are in the water. You see a lifeboat and some floating debris",
            "Swim to the lifeboat", "lifeboat",
            "Cling to the debris", "debris"
        ),
        "lifeboat": (
            "You climb into safety in the boat. So does everyone else, and the boat slowly begins to sink",
            "Start over", "start",
            "Quit", "quit"
        ),
        "debris": (
            "The debris isn't much, but eventually you feel sand beneath your feet. You are on an island!",
            "Look for wreckage or survivors", "search",
            "Explore your new surroundings", "explore"
        ),
        "search": (
            "You see enough wreckage to build a simple shelter, but sadly no survivors.",
            "Get some rest", "rest",
            "Explore the island to look for food", "explore"
        ),
        "explore": (
            "In your exhausted state, you look around the island. But you fail to notice the cliff.",
            "Start over", "start",
            "Quit", "quit"
        ),
        "rest": (
            "You feel surprisingly well-rested after a night in your shelter.",
            "Build a fire", "fire",
            "Look for food", "food"
        ),
        "fire": (
            "It's very difficult to start a fire without matches",
            "Give up", "food",
            "Keep trying", "fire"  # Creates a loop until player gives up
        ),
        "food": (
            "You find some berries. On the way back you see a box that washed ashore with matches!",
            "Keep looking for food", "food2",
            "Try again to start the fire", "fire2"
        ),
        "food2": (
            "You keep looking for food but don't find anything. You get lost and never return.",
            "Start over", "start",
            "Quit", "quit"
        ),
        "fire2": (
            "You get the fire lit. In the distance, you see a dot on the horizon.",
            "Swim to the ship", "swim2",
            "Make the fire larger", "signal"
        ),
        "swim2": (
            "You swim to the boat, but it's farther than you thought. You lose.",
            "Start over", "start",
            "Quit", "quit"
        ),
        "signal": (
            "You build the fire larger. The ship notices you. You are saved!",
            "Start over", "start",
            "Quit", "quit"
        )
    }

def playNode(node_name, game_data):
    """
    Processes the current node, displays options, and returns the next node
    Implements exception handling for invalid nodes
    """
    try:
        node = game_data[node_name]
    except KeyError:
        print("Error: Invalid node encountered. Restarting game.")
        return "start"
    
    # Unpack node data
    description, menuA, nodeA, menuB, nodeB = node
    
    # Display current node information
    print("\n" + description)
    
    # Handle terminal nodes (only two options are start/quit)
    if nodeA == "start" and nodeB == "quit":
        print("1. " + menuA)
        print("2. " + menuB)
        choice = getValidChoice(1, 2)
        return nodeA if choice == 1 else nodeB
    
    # Handle regular nodes
    print("\nWhat will you do?")
    print("1. " + menuA)
    print("2. " + menuB)
    choice = getValidChoice(1, 2)
    
    return nodeA if choice == 1 else nodeB

def getValidChoice(min_option, max_option):
    """
    Handles user input with validation and exception handling
    Returns a valid integer choice between min and max
    """
    while True:
        try:
            choice = int(input(f"Enter your choice ({min_option}-{max_option}): "))
            if min_option <= choice <= max_option:
                return choice
            else:
                print(f"Please enter a number between {min_option} and {max_option}")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the game
if __name__ == "__main__":
    main()