#########################################################################
# A Character Creator program for a role-playing game.                  #
# The player is given a pool of 30 points to spend on four attributes:  #
# Strength, Health, Wisdom, and Dexterity.                              #
# The player is able to spend points from the pool on any attribute and #
# is also able to take points from an attribute and put them back into  #
# the pool.                                                             #
#########################################################################

#############
# FUNCTIONS #
#############

# Main menu of program
def main_menu(point_pool, dict_attributes):
    print("\n\n\t{:7}Available Points ({})".format(" ", point_pool))
    print("\n\tEnter:")
    for attribute, info in dict_attributes.items():
        name = ""
        points = 0
        char = ''
        for i in info:
            name = info["name"]
            points = info["points"]
            char = info["char"]
        print("\t{:7}'{}' for {:11}({})".format(" ", char, name, points))
    print("\t{:7}'x' to exit the program".format(" "))
    choice = input("\nMake your selection: ")
    return choice

# Prompts user for points amount to update
def prompt_for_points(att_name, att_value, point_pool):
    print("\n\nAvailable Points: {}".format(point_pool))
    print("\t{}: {}".format(att_name, att_value))
    print("\nHow many point would you like to add or remove?")
    print("\tEnter a positive number to add points.")
    print("\tEnter a negative number to remove points.")
    print("\nAssign points to {}:".format(att_name), end=" ")
    user_input = int(input())
    return user_input

# Assigns points amount to update
# Determines if points amount valid
def assign_points(att_name, att_value, point_pool, total_points, user_input):
    choice = ""
    isUpdated = False

    while (choice != 'x'):
        if (((point_pool - user_input) <= total_points) and
            ((point_pool - user_input) >= 0) and
            (att_value + user_input >= 0)):
            att_value = int(att_value + user_input)
            isUpdated = True
            break
        else:
            if (((point_pool - user_input) > total_points) or
                 (att_value + user_input < 0)):
                print("\nYou do not have enough {} points available for "
                      "that.".format(att_name))
                print("Available {} Points: {}".format(att_name, att_value))
            else:
                print("\nYou do not have points available for that.")
                print("Available Points:", point_pool)
            # Prompts user for valid choice
            choice = input("\nEnter a valid value or press 'x' to return "
                           "to the main menu. ")
            while (choice != 'x'):
                try:
                    user_input = int(choice)
                    break
                except:
                    if (choice == 'x'):
                        break
                    else:
                        print("Please make a valid selection.")
                        choice = input("\nEnter a valid value or press 'x' to "
                                   "to return to the main menu. ")
            input("\nPress enter to continue.")
    return [att_value, user_input, isUpdated]

# Updates point pool if points amount valid
def update_point_pool(point_pool, user_input, isUpdated):
    if (isUpdated == True):
        print(point_pool, "Before")
        point_pool = point_pool - user_input
        print(point_pool, "After")
    else:
        point_pool = point_pool
    return point_pool

# Displays values of character attributes
def view_points(dict_character):
    print("\n")
    for attribute, info in dict_character.items():
        name = ""
        points = 0
        for i in info:
            name = info["name"]
            points = info["points"]
        print("\t{:11}({})".format(name, points))
    print(" Available Points  ({})".format(point_pool))


#############
# VARIABLES #
#############

# Points Variables
total_points = 30
point_pool = total_points

# Default attributes and values
dict_attributes = {
    "attribute1" : {
    "name" : "Strength",
    "char" : 's',
    "points" : 0
    },
    "attribute2" : {
    "name" : "Health",
    "char" : 'h',
    "points" : 0
    },
    "attribute3" : {
    "name" : "Wisdom",
    "char" : 'w',
    "points" : 0
    },
    "attribute4" : {
    "name" : "Dexterity",
    "char" : 'd',
    "points" : 0
    }
    }

num_attributes = len(dict_attributes)      # Attributes quantity
dict_character = dict_attributes.copy()    # Stores character's attributes

# Variables used for updating attributes
temp_attribute_list = ()
isUpdated = False       # Determines if attribute points updated

choice = ""    # Variable for menu choice selection

# Introduction
print("\n\nYou have a pool of {} points to spend on {} attributes: {}, {}, "
      "{}, and {}.\nYou are able to spend points from the pool on any "
      "attribute as well as reassign points as you see fit.".format(
       total_points, num_attributes,
       dict_attributes["attribute1"]["name"],
       dict_attributes["attribute2"]["name"],
       dict_attributes["attribute3"]["name"],
       dict_attributes["attribute4"]["name"]))
input("\nPress enter to continue.")

# Main menu
while (choice != 'x'):
    choice = main_menu(point_pool, dict_attributes)

    # Attribute 1
    if (choice == dict_character["attribute1"]["char"]):
        user_input = prompt_for_points(dict_character["attribute1"]["name"],
                                       dict_character["attribute1"]["points"], 
                                       point_pool)
        temp_attribute_list = assign_points(
                                dict_character["attribute1"]["name"],
                                dict_character["attribute1"]["points"],
                                point_pool, total_points, user_input)
        updated_points = temp_attribute_list[0]
        dict_character["attribute1"].update({"points": updated_points})
        point_pool = update_point_pool(point_pool, temp_attribute_list[1],
                                        temp_attribute_list[2])

    # Attribute 2
    elif (choice == dict_character["attribute2"]["char"]):
        user_input = prompt_for_points(dict_character["attribute2"]["name"],
                                       dict_character["attribute2"]["points"], 
                                       point_pool)
        temp_attribute_list = assign_points(
                                dict_character["attribute2"]["name"],
                                dict_character["attribute2"]["points"],
                                point_pool, total_points, user_input)
        updated_points = temp_attribute_list[0]
        dict_character["attribute2"].update({"points": updated_points})
        point_pool = update_point_pool(point_pool, temp_attribute_list[1],
                                        temp_attribute_list[2])

    # Attribute 3
    elif (choice == dict_character["attribute3"]["char"]):
        user_input = prompt_for_points(dict_character["attribute3"]["name"],
                                       dict_character["attribute3"]["points"], 
                                       point_pool)
        temp_attribute_list = assign_points(
                                dict_character["attribute3"]["name"],
                                dict_character["attribute3"]["points"],
                                point_pool, total_points, user_input)
        updated_points = temp_attribute_list[0]
        dict_character["attribute3"].update({"points": updated_points})
        point_pool = update_point_pool(point_pool, temp_attribute_list[1],
                                        temp_attribute_list[2])

    # Attribute 4
    elif (choice == dict_character["attribute4"]["char"]):
        user_input = prompt_for_points(dict_character["attribute4"]["name"],
                                       dict_character["attribute4"]["points"], 
                                       point_pool)
        temp_attribute_list = assign_points(
                                dict_character["attribute4"]["name"],
                                dict_character["attribute4"]["points"],
                                point_pool, total_points, user_input)
        updated_points = temp_attribute_list[0]
        dict_character["attribute4"].update({"points": updated_points})
        point_pool = update_point_pool(point_pool, temp_attribute_list[1],
                                        temp_attribute_list[2])

    # Exits the program
    elif choice == 'x':
        print("\n\nYour character has:")
        view_points(dict_character)
        input("\nPress enter to exit.")
        break

    # Invalid entry
    else:
        print("Please make a valid selection.")
        input("\nPress enter to continue.")

    '''
    # Health
    elif choice == 'h':
        user_input = prompt_for_points("Health", health, point_pool)
        temp_attribute_list = assign_points("Health", health, point_pool, total_points, user_input)
        health = temp_attribute_list[0]
        point_pool = update_point_pool(point_pool, temp_attribute_list[1],
                                       temp_attribute_list[2])

    # Wisdom
    elif choice == 'w':
        user_input = prompt_for_points("Wisdom", wisdom, point_pool)
        temp_attribute_list = assign_points("Wisdom", wisdom, point_pool, total_points, user_input)
        wisdom = temp_attribute_list[0]
        point_pool = update_point_pool(point_pool, temp_attribute_list[1],
                                       temp_attribute_list[2])

    # Dexterity
    elif choice == 'd':
        user_input = prompt_for_points("Dexterity", dexterity, point_pool)
        temp_attribute_list = assign_points("Dexterity", dexterity, point_pool, total_points, user_input)
        dexterity = temp_attribute_list[0]
        point_pool = update_point_pool(point_pool, temp_attribute_list[1],
                                       temp_attribute_list[2])
    '''