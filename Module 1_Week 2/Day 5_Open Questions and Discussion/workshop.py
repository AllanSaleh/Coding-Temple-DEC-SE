while True:
    print("""
Welcome!
    1. Enter your name
    2. What's your favorite sports team?
    3. Exit
""")
    
    user_input = int(input("What would you like to choose? (1,2, or 3)"))
    if user_input == 1:
        user_name = input("Enter your name: ")
        print(f"Nice to meet you {user_name}")
    elif user_input == 2:
        fav_team = input("Enter your fav team: ")
        print("Nice! I like "+ fav_team +" as well!")
    elif user_input == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice")




def average(num1, num2, num3):
    return (num1+num2+num3)/3


average_of_3numbers = average(10, 5 ,9)

print(f"The average of the 3 numbers is {average_of_3numbers}")

average_of_3numbers2 = average(50, 222 ,5)

print(f"The average of the 3 numbers is {average_of_3numbers2}")



user_num1 = int(input("Enter the first number: "))
user_num2 = int(input("Enter the second number: "))
user_num3 = int(input("Enter the third number: "))

average_of_users_nums = average(user_num1, user_num2, user_num3)

print(f"The average of the 3 users numbers is {average_of_users_nums}")
