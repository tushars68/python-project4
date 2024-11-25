def start_game():
    print("Welcome to the Adventure!")
    print("You find yourself in a dark forest.")
    print("There's a path to the left and a path to the right.")
    choice = input("Which path do you take? (left/right): ")

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def left_path():
    print("You follow the left path and encounter a dragon.")
    print("What do you do?")
    print("1. Fight the dragon")
    print("2. Run away")
    choice = input("Choose an action (1/2): ")

    if choice == "1":
        print("You bravely face the dragon, but it's too powerful. Game Over.")
    elif choice == "2":
        print("You turn back and escape the dragon. You win!")
    else:
        print("Invalid choice. You're eaten by the dragon. Game Over.")

def right_path():
    print("You follow the right path and discover a hidden treasure chest.")
    print("Congratulations! You've won the game!")

start_game()