# Floating vs Int using isinstance()
NUM_INT = 42
num_float = 42.42
print(isinstance(NUM_INT, int))
print(isinstance(NUM_INT, float))
print(isinstance(num_float, int))
print(isinstance(num_float, float))

print("-" * 30)



# Basic Arithmetic (+ - / *) and format specifiers
drink_price = 3.252325165
cups_drunk = 3
total_spent = drink_price * cups_drunk

print(f'Total spent on drinks today: ${total_spent:.2f}')

''' Different parts of the format specifier
 : - starts the format specifier
 .2 - specifies that two decimal places should be displayed
 f -  tells Python to format the number as a float
'''

print("-" * 30)

# Modulus (%) - gives the remainder of two values
num = 21
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    
print(4%2)

hour = 21
hour_on_clock = hour % 12
print(hour_on_clock)


wallet = 100
childs_dream = 87.52
left_after_dream = wallet % childs_dream
print(f"Left in wallet after spoiling child: ${left_after_dream:.2f}")

print("-" * 30)

# Floor Division (//) rounds the answer down
people = 5
slices_of_pizza = 12
slices_per_person = slices_of_pizza // people
print("Slices of pizza each person gets:", slices_per_person)

print("-" * 30)

# Exponents ** and pow()
square_of_two = 2 ** 2
print(square_of_two)

cube_of_two = 2 ** 3
print(cube_of_two)

big_math = pow(2, 3, 5)  # 2 ^ 3 % 5
big_math2 = 2 ** 3 % 5
print(big_math)
print(big_math)


print("-" * 30)


# Absolute values
city_1_temp = 30
city_2_temp = 22

# We don't care which one is higher 
# We just want the difference between the two
temp_difference = abs(city_2_temp - city_1_temp)
print(f"The difference between the two cities: {temp_difference}")

print("-" * 30)



# Rounding with round()
price_of_item1 = 7.456
rounded_price1 = round(price_of_item1)
print("Round down price:", rounded_price1)

price_of_item2 = 7.556
rounded_price2 = round(price_of_item2)
print("Round down price:", rounded_price2)

price_of_item3 = 7.556
rounded_price3 = round(price_of_item3, 2)
print("Round down price:", rounded_price3)

print("-" * 30)

# Converting to Integer - int() and float()
floating_price = 4.99
approx_price = int(floating_price)
print("Approximate integer price", approx_price)

string_price = "4.99"
float_price = float(floating_price)
print("Approximate integer price", approx_price)
print("Approximate float price", float_price)

print(isinstance(float_price,float))

number = "54"
number_int = int(number)
print(number_int*3)
print("-" * 30)


# max() and min()
knight_strength = 20
dragon_strength = 50
grandma_strength = 100

print(max(knight_strength, dragon_strength, grandma_strength))
print(min(knight_strength, dragon_strength, grandma_strength))

print("-" * 30)