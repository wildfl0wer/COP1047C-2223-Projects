import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import *


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

#################
# GUI INTERFACE #
#################
window = tk.Tk()

# Determines window size
window.geometry('800x600')

greeting = tk.Label(text ="\nYou have a pool of {} points to spend on {} attributes: {}, {}, "
      "{}, and {}.\nYou are able to spend points from the pool on any "
      "attribute as well as reassign points as you see fit.\n".format(
       total_points, num_attributes,
       dict_attributes["attribute1"]["name"],
       dict_attributes["attribute2"]["name"],
       dict_attributes["attribute3"]["name"],
       dict_attributes["attribute4"]["name"]))

greeting.pack()

# Can use this to modify attributes
sb = Spinbox(from_ = 1, to = total_points) 
sb.pack()

# Can use this to modify attributes
# create a combobox
selected_value = tk.StringVar()
combo = ttk.Combobox(window, textvariable=selected_value)
combo.pack()
#combo['values']= (1, 2, 3, 4, 5)
list = [*range(1, total_points + 1, 1)]
combo['values']= list
combo.current(9)
# prevent typing a value
combo['state'] = 'readonly'
#combo.current(int(len(list)/2)) #set the selected item
#combo.grid(column=0, row=0)
health = selected_value.get()

# bind the selected value changes
def combo_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_value.get()}!'
    )
    health = selected_value.get()
    display_health = tk.Label(text="Health: {}".format(health))
    display_health.pack()    # Will display each time changed

combo.bind('<<ComboboxSelected>>', combo_changed)

window.mainloop()  # Needs to be at end of Python file for Tkinter to run