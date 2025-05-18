import random


fortunes = [
    "It is certain.",
    "Ask again later.",
    "My reply is no.",
    "Yes, definitely.",
    "Cannot predict now.",
    "Oulook is good.",
    "Very doubtful.",
    "Signs point to yes.",
    "Better not tell you now.",
    "Don't count on it."
]


print("What will you do?")
print("1: print all the fortunes")
print("2: print a specific fortune")
print("3: receive a random fortune")

userInput = input("Please choose 1, 2, or 3: ")

try:
    choice = int(userInput)
except ValueError:
    print("Invalid input. Please enter a number from 1 to 3.")
    exit()

if choice == 1:
    print("Your fortunes:")
    for index in range(len(fortunes)):
        print(f"{index}) {fortunes[index]}")


elif choice == 2:
    indexInput = input("What number will you choose? (0-10): ")
    try:
        index = int(indexInput)
        if 0 <= index < len(fortunes):
            print(fortunes[index])
        else:
            print("Invalid number. Must be between 0 and 7.")
    except ValueError:
        print("Invalid input. Please enter a valid number. ")


elif choice == 3:
    question = input("Your question: ")
    randomIndex = random.randint(0, len(fortunes) - 1)
    print(fortunes[randomIndex])


else:
    print("Invalid menu choice. Please select 1, 2, or 3. ")
    