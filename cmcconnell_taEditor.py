import json

def main():
    game = getDefaultGame()
    keepGoing = True
    
    while keepGoing:
        try:
            choice = getMenuChoice()
            
            if choice == "1":    # Play
                playGame(game)
            elif choice == "2":  # Edit
                node = editNode(game)
                if node:
                    game[node["name"]] = node
            elif choice == "3":  # Save
                saveGame(game)
            elif choice == "4":  # Load
                game = loadGame()
            elif choice == "5":  # Quit
                keepGoing = False
                print("Thanks for using the Text Adventure Editor!")
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def getMenuChoice():
    print("\n=== Text Adventure Editor ===")
    print("1. Play Game")
    print("2. Edit Node")
    print("3. Save Game")
    print("4. Load Game")
    print("5. Quit")
    return input("Choose an option: ")

def playGame(game):
    currentNode = "start"
    print("\n=== Starting Game ===")
    
    while currentNode != "quit":
        try:
            currentNode = playNode(game, currentNode)
        except Exception as e:
            print(f"Error playing node: {str(e)}")
            break
    
    print("\nGame Over!")

def playNode(game, nodeName):
    if nodeName not in game:
        print(f"Error: Node '{nodeName}' not found!")
        return "quit"
    
    node = game[nodeName]
    print(f"\n{node['text']}")
    
    if "choices" not in node or not node["choices"]:
        return "quit"
    
    while True:
        try:
            print("\nChoices:")
            for i, choice in enumerate(node["choices"], 1):
                print(f"{i}. {choice['text']}")
            
            choice = int(input("\nEnter your choice (number): ")) - 1
            if 0 <= choice < len(node["choices"]):
                return node["choices"][choice]["destination"]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def getDefaultGame():
    return {
        "start": {
            "name": "start",
            "text": "Welcome to your new adventure!",
            "choices": [
                {
                    "text": "End game",
                    "destination": "quit"
                }
            ]
        }
    }

def editNode(game):
    try:
        print("\nCurrent game structure:")
        print(json.dumps(game, indent=2))
        
        nodeName = input("\nEnter node name to edit (or create): ").strip()
        if not nodeName:
            print("Node name cannot be empty.")
            return None
        
        if nodeName in game:
            newNode = game[nodeName].copy()
            print(f"Editing existing node: {nodeName}")
        else:
            newNode = {
                "name": nodeName,
                "text": "",
                "choices": []
            }
            print(f"Creating new node: {nodeName}")
        
        newNode["text"] = editField("text", newNode.get("text", ""))
        
        while True:
            try:
                choiceCount = int(input("\nHow many choices for this node? "))
                if choiceCount >= 0:
                    break
                print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")
        
        newNode["choices"] = []
        for i in range(choiceCount):
            choice = {}
            print(f"\nChoice {i+1}:")
            choice["text"] = editField("choice text", "")
            choice["destination"] = editField("destination node", "")
            newNode["choices"].append(choice)
        
        return newNode
        
    except Exception as e:
        print(f"Error editing node: {str(e)}")
        return None

def editField(fieldName, currentValue):
    print(f"Current {fieldName}: {currentValue}")
    newValue = input(f"Enter new {fieldName} (or press Enter to keep current): ").strip()
    return newValue if newValue else currentValue

def saveGame(game):
    try:
        with open('game.dat', 'w') as file:
            json.dump(game, file, indent=2)
        print("Game saved successfully to 'game.dat'!")
    except Exception as e:
        print(f"Error saving game: {str(e)}")

def loadGame():
    try:
        with open('game.dat', 'r') as file:
            game = json.load(file)
        print("Game loaded successfully from 'game.dat'!")
        return game
    except FileNotFoundError:
        print("No saved game found. Starting with default game.")
        return getDefaultGame()
    except Exception as e:
        print(f"Error loading game: {str(e)}")
        return getDefaultGame()

if __name__ == "__main__":
    main()
