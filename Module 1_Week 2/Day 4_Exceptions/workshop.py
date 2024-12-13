try:
    user_choice = int(input("What number would you like to cube?\n"))
    print(user_choice**3)
except ValueError:
    print('Not a valid choice')

try:
    user_choice = int(input("What number would you like to divide?\n"))
    print(user_choice/0)
except ZeroDivisionError:
    print('Cannot divide number with zero')




def duel_opponent(opponent):
    try:
        skill_level = int(input("Enter your skill level "
                            "(0 - Novice | 1 - Warrior | 2 - Champion)"))
        result = 100 / skill_level

    except ZeroDivisionError:
        print("Novices are too inexperienced, you were defeated.")
    except ValueError:
        print("Invalid skill level input! Please enter a number.")
    else:
        print(f"You defeated {opponent} with {result:.2f} of your strength remaining.")
    finally:
        print("Thanks for playing!")


# Main menu
user_input = 0
while user_input != 2:
    print('''
    \nMain menu
    1. Duel an opponent
    2. Exit  
''')
    
    try:
        user_input = int(input("Please choose an option (1 or 2):"))
    except ValueError:
        print("The input cannot be empty. Try again")

    if user_input == 1:
        try:
            opponent_name = input("Enter your opponent:")

            if not opponent_name.strip():
                raise ValueError("Opponent's name cannot be empty!")
        except ValueError as e:
            print(e)
        else:
            duel_opponent(opponent_name)
    elif user_input == 2:
        print("Goodbye! Good luck!")