# functions.py: function definitions for csw8 final project

# displays the menu options for the user to select, no return
def print_main_menu(menu_options):
  print("=======================")
  for i in menu_options:
    print(f" {i} - {menu_options[i]} ")
  print("=======================")