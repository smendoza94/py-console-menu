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
      break # exit the main `while` loop
    else:
      if opt in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
        print(f"You selected option {opt} to > {the_menu[opt]}.")
      else:
        print(f"WARNING: {opt} is an invalid option.\n")
    time.sleep(1)
  print("Have a delicious day!")

# store menu item information that the users can view and maintain by 
# adding and editing entries.

# save the state of the system entries by saving the information to file 
# and later retrieving from it.