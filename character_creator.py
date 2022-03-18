##########
# A Character Creator program for a role-playing game.
# The player is given a pool of 30 points to spend on four attributes:
# Strength, Health, Wisdom, and Dexterity.
# The player is able to spend points from the pool on any attribute and
# is also able to take points from an attribute and
# put them back into the pool.
##########

# Main menu of program
def main_menu(point_pool, strength, health, wisdom, dexterity):
    print("\n\n\t        Available Points ({})".format(point_pool))
    print("\n\tEnter: 's' for Strength  ({})".format(strength))
    print("\t       'h' for Health    ({})".format(health))
    print("\t       'w' for Wisdom    ({})".format(wisdom))
    print("\t       'd' for Dexterity ({})".format(dexterity))
    print("\t       'x' to exit the program")
    choice = input("\nMake your selection: ")
    return choice

# Prompts user for points
def prompt_for_points(att_name, att_value, point_pool):
    print("\n\nAvailable Points: {}".format(point_pool))
    print("\t{}: {}".format(att_name, att_value))
    print("\nHow many point would you like to add or remove?")
    print("\tEnter a positive number to add points.")
    print("\tEnter a negative number to remove points.")
    print("\nAssign points to {}:".format(att_name), end=" ")
    user_input = int(input())
    return user_input

# Determines if points amount valid
# If valid points are update. Otherwise points unchanged.
def assign_points(att_name, att_value, point_pool, total_points, user_input):
    if (((point_pool - user_input) < total_points) and
        ((point_pool - user_input) >= 0) and
        (att_value + user_input >= 0)):

        att_value = int(att_value + user_input)

    else:
        if (((point_pool - user_input) > total_points) or
             (att_value + user_input < 0) or
             (att_value + user_input < 0)):

            print("\nYou do not have enough {} points for that.".format(att_name))
            print("Available {} Points: {}".format(att_name, att_value))

        else:
            print("\nYou do not have enough points left for that.")
            print("Available Points:", point_pool)

        att_value = att_value
        input("\nPress enter to continue.")

    return att_value

# Updates point pool if points amount valid
def update_point_pool(att_value, point_pool, total_points, user_input):
    if (((point_pool - user_input) < total_points) and
        ((point_pool - user_input) >= 0) and
        (att_value + user_input >= 0)):

        point_pool = point_pool - user_input

    else:
        point_pool = point_pool

    return point_pool

# Displays values of attributes
def view_points(strength, health, wisdom, dexterity):
    print("\n\tStrength  ({})".format(strength))
    print("\tHealth    ({})".format(health))
    print("\tWisdom    ({})".format(wisdom))
    print("\tDexterity ({})".format(dexterity))
    print(" Available Points ({})".format(point_pool))

# Points Variables
total_points = 30
point_pool = total_points

# Dictionary with initial attribute values
dict_attributes = {
    "Strength": 0, 
    "Health": 0, 
    "Wisdom": 0, 
    "Dexterity": 0
    }

# List with attribute names
# Reflects keys in dictionary
list_attributes = list (dict_attributes.keys())
num_attributes = len(list_attributes)

# Attribute variables
# Should be written in same order as in dictionary for consistency
strength = dict_attributes["Strength"]
health = dict_attributes["Health"]
wisdom = dict_attributes["Wisdom"]
dexterity = dict_attributes["Dexterity"]

choice = ""    # Variable for menu choice selection

print("\n\nYou have a pool of {} points to spend on {} attributes: {}, {}, "
      "{}, and {}.\nYou are able to spend points from the pool on any "
      "attribute as well as reassign points as you see fit.".format(
      total_points, num_attributes, list_attributes[0],list_attributes[1],
      list_attributes[2], list_attributes[3]))
input("\nPress enter to continue.")

while (choice != 'x'):
    choice = main_menu( point_pool, strength, health, wisdom, dexterity )

    # Strength
    if choice == 's':
        user_input = prompt_for_points("Strength", strength, point_pool)
        strength = assign_points("Strength", strength, point_pool, total_points, user_input)
        point_pool = update_point_pool(strength, point_pool, total_points, user_input)
    # Health
    elif choice == 'h':
        user_input = prompt_for_points("Health", health, point_pool)
        health = assign_points("Health", health, point_pool, total_points, user_input)
        point_pool = update_point_pool(health, point_pool, total_points, user_input)

    # Wisdom
    elif choice == 'w':
        user_input = prompt_for_points("Wisdom", wisdom, point_pool)
        wisdom = assign_points("Wisdom", wisdom, point_pool, total_points, user_input)
        point_pool = update_point_pool(wisdom, point_pool, total_points, user_input)

    # Dexterity
    elif choice == 'd':
        user_input = prompt_for_points("Dexterity", dexterity, point_pool)
        dexterity = assign_points("Dexterity", dexterity, point_pool, total_points, user_input)
        point_pool = update_point_pool(dexterity, point_pool, total_points, user_input)

    # Exits the program
    elif choice == 'x':
        print("\n\nYour character has:")
        view_points(strength, health, wisdom, dexterity)
        input("\nPress enter to exit.")
        break

    # Invalid entry
    else:
        print("Please make a valid selection.")
        input("\nPress enter to continue.")