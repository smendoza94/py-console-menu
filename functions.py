# functions.py: function definitions for csw8 final project

# displays the menu options for the user to select, no return
def print_main_menu(menu_options):
  print("=======================")
  for i in menu_options:
    print(f" {i} - {menu_options[i]} ")
  print("=======================")

def list_helper(list_menu, restaurant_menu_list, spicy_scale_map):
  if len(restaurant_menu_list) == 0:
    print("WARNING: There is nothing to display!")
    # Pause before going back to the main menu
    input("::: Press Enter to continue")
  else:
    subopt = get_selection("List", list_menu)
    if subopt == 'A':
      print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1)
    elif subopt == 'V':
      print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1, vegetarian_only=True)

def get_selection(action, suboptions, to_upper=True, go_back=False):
  # param: action (string) - the action that the user would like to perform; printed in function prompt.
  # param: suboptions (dictionary) - contains suboptions that are listed underneath the function prompt.
  # param: to_upper (Boolean) - by default, set to True, so the user selection is converted to upper-case.
  #   If set to False, then the user input is used as-is.
  # param: go_back (Boolean) - by default, set to False. If set to True, then allows the user to select 
  #   the option M to return back to the main menu
  # The function displays a submenu for the user to choose from. Asks the user to select an option using 
  #   the input() function. Re-prints the submenu if an invalid option is given. Prints the confirmation 
  #   of the selection by retrieving the description of the option from the suboptions dictionary.
  # returns: the option selection (by default, an upper-case string). The selection be a valid key in the 
  #   suboptions or a letter M, if go_back is True.

  selection = None
  if go_back:
    if 'm' in suboptions or 'M' in suboptions:
      print("Invalid submenu, which contains M as a key.")
      return None
  while selection not in suboptions:
    print(f"::: What field would you like to {action.lower()}?")
    for key in suboptions:
      print(f"{key} - {suboptions[key]}")
    if go_back:
      selection = input(f"::: Enter your selection "
        f"or press 'm' to return to the main menu\n> ")
    else:
      selection = input("::: Enter your selection\n> ")
    if to_upper:
      selection = selection.upper()  # to allow us to input lower- or upper-case letters
    if go_back and selection.upper() == 'M':
      return 'M'

  print(f"You selected |{selection}| to",
    f"{action.lower()} |{suboptions[selection]}|.")
  return selection

def print_restaurant_menu(restaurant_menu, spicy_scale_map, name_only=False, show_idx=True, start_idx=0, vegetarian_only=False):
  # param: restaurant_menu (list) - a list object that holds the dictionaries for each dish.
  # param: spicy_scale_map (dict) - a dictionary object that is expected to have the integer keys that 
  #   correspond to the "level of spiciness."
  # param: name_only (Boolean). If False, then only the name of the dish is printed. Otherwise, displays 
  #   the formatted dish information.
  # param: show_idx (Boolean). If False, then the index of the menu is not displayed. Otherwise, displays 
  #   the "{idx + start_idx}." before the dish name, where idx is the 0-based index in the list.
  # param: start_idx (int). an expected starting value for idx that gets displayed for the first dish, 
  #   if show_idx is True.
  # param:  vegetarian_only (Boolean). If set to False, prints all dishes, regardless of their 
  #   is_vegetarian status ("yes/no" field status). If set to True , display only the dishes with
  #   "is_vegetarian" status set to "yes".
  # returns: None; only prints the restaurant menu

  print('------------------------------------------')
  # Go through the dishes in the restaurant menu:
  for i in restaurant_menu: 
    # if vegetarian_only is True and the dish is not vegetarian, skip this iteration
    if vegetarian_only and i["is_vegetarian"] == "no":
      continue

    # if the index of the task needs to be displayed (show_idx is True), print dish index only
    food_name = i["name"].upper()
    if show_idx == True:
      print(f"{restaurant_menu.index(i)+1}. {food_name}")
    else:
      # print the name of the dish
      print(f"{food_name}")
    
    # if name_only is False
    if not name_only:
      print("* Calories: " + str(i["calories"]))
      print("* Price: " + str(i["price"]))
      print("* Is it vegetarian: " + str(i["is_vegetarian"]))
      print("* Spicy level: "+ str(spicy_scale_map[i["spicy_level"]]))