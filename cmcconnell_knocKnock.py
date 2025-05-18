userName = input("What is your name? ")
print(f"Hello {userName},  do you want to hear a joke? (Y/N)")
userResponse = input()
if userResponse == "yes":
    print("Knock Knock")
    response1 = input()
    if response1 == "Who's there":
        print("Lettuce")
        response2 = input()
        if response2 == "Lettuce who?":
            print("Lettuce in, it's cold out here!")
        else:
            print("You were supposed to say 'lettuce who?' ")
    else:
        print("You were supposed to say, Who's there? ")
elif userResponse == "no":
    print("You are no fun.")
else:
    print("I do not understand. ")
            