from functions import *
import time

if __name__ == "__main__":
  # list the options for the user to select from
  the_menu = {  
    "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "M" : "Show average price",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program",
  } 

  # list containing the menu item information dictionaries 
  restaurant_menu_list = [
    {
      "name": "burrito",
      "calories": 500,
      "price": 12.90,
      "is_vegetarian": "yes",
      "spicy_level": 2
    },
    {
      "name": "rice bowl",
      "calories": 400,
      "price": 14.90,
      "is_vegetarian": "no",
      "spicy_level": 3
    },
    {
      "name": "margherita",
      "calories": 800,
      "price": 18.90,
      "is_vegetarian": "no",
      "spicy_level": 2
    }
  ]

  # "List" menu sub-options for user to select from
  list_menu = {
    "A": "complete menu",
    "V": "vegetarian dishes only",
  }

  # contain the mapping of the spicy_level values, as integers, to a string 
  # for the name of the spice level
  spicy_scale_map = {
    1: "Not spicy",
    2: "Low key spicy",
    3: "Hot",
    4: "Diabolical",
  }

  # initilize the user opt, default NULL "no selection made"
  opt = None

  # initializes the interface that allows users to interact with the system
  while True:
    # call the print_main_menu() to display the menu options in the console
    print_main_menu(the_menu) 
    print("::: Enter an option")
    
    opt = input("> ").upper()

    # if the user selects "Q" quit the program 
    if opt == "Q": 
      print("Goodbye!\n")
      # exit the main `while` loop
      break
    elif opt == 'L':
      list_helper(list_menu, restaurant_menu_list, spicy_scale_map)
    elif opt == 'A':
      add_helper(restaurant_menu_list, spicy_scale_map)
    else:
      # check of the character stored in opt is in the_menu dictionary then
      # provide feedback of the option selection and if its valid option
      if opt in the_menu: 
        print(f"You selected option {opt} to > {the_menu[opt]}.")
      else:
        print(f"WARNING: {opt} is an invalid option.\n")
    time.sleep(1)
  # print("Have a delicious day!")

# store menu item information that the users can view and maintain by 
# adding and editing entries.

# save the state of the system entries by saving the information to file 
# and later retrieving from it.