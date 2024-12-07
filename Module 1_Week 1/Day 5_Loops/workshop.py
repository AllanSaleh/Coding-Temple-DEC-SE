import time

characters = [
    "Luke Skywalker",
    "Darth Vader",
    "Yoda",
    "Leia Organa",
    "Han Solo",
    "Emperor Palpatine",
    "Chewbacca",
]

for character in characters:
    print(character)

print('-'*30)

for i in range(0, len(characters)):
   print(f"{i+1} - {characters[i]}") 

print('-'*30)

# enumerate separates index and value
for index, name in enumerate(characters):
    print("Index:", index)
    print(name)

print('-'*30)

print("Preparing for light speed jump!")
for second in range(5,0,-1):
    print(f"{second}...")
    time.sleep(1) #Pause for 1 second
print("Light speed jump activated! VROOM!")

print('-'*30)

print("Who will bring the balance to the force?")
for character in characters:
    if character == "Darth Vader":
        print(f"{character} brought balance to the force but at a great cost")
    elif character == "Emperor Palpatine":
        print(f"{character} is pure evil! He will not balance anything!")
    else:
        print(f"{character} is probably an ally!")

print('-'*30)

weapons = ["lightsaber", "force choke", "force push", "blaster"]

for weapon, character in zip(weapons, characters):
    print(f"{weapon} protects {character}")


# tracker = True
counter = 1

while counter <=5:
    print("Hello", counter)
    counter += 1

print('-'*30)


force_level = 0
target_force_level = 10

print("Jedi training started...")
while True:
    print(f"Force level: {force_level}. Training intensifies!!")
    force_level += 1
    if force_level == 3:
        print("You can lift rocks! You feel the force growing stronger!")
        continue
    if force_level == 6:
        print("You can lift your space ship and do front flips with Yoda on your back!")
        continue
    elif force_level == target_force_level:
        print("Training complete! You are now a Jedi Knight, Yoda is pleased")
        break
    