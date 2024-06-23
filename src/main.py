from math import sqrt, pow

user_diameter = int(input("Enter the diameter of the circle: "))

if type(user_diameter) != int:
    print("Please enter a valid number")
    exit()
    
if user_diameter % 2 == 0:
    print("Please enter an odd number")
    exit()

user_radius = user_diameter / 2

for i in range(user_diameter):
    for j in range(user_diameter):
        if sqrt(pow(j - int(user_radius), 2) + pow(i - int(user_radius), 2)) <= user_radius:
            print("* ", end="")
        else:
            print("  ", end="")
    print()