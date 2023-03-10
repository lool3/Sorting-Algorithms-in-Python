def menu(menuOptions):
  while True:
    print("----------Main-Menu----------\n")
    for i, option in enumerate(menuOptions.keys()):
      print(f"{i+1}. {option}")
    print(f"{len(menuOptions) + 1}. Exit")
    print("\n-----------------------------\n")
    try:
      menuChoice = int(input("Choice: "))
    except ValueError:
      print("That's not even a number!")
      continue
    else:
      if menuChoice == len(menuOptions) + 1:
        exit("Goodbye!")
      elif menuChoice not in range(1, len(menuOptions) + 1):
        print("That's not an option!")
        continue
    
    return list(menuOptions.values())[menuChoice - 1]
