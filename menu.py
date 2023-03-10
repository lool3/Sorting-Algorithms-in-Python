def menu(menuOptions):
  while True:
    print("----------Main-Menu----------\n")
    for i, option in enumerate(menuOptions.keys()):
      print(f"{i+1}. {option}")

    try:
      menuChoice = int(input("\nChoice: "))
    except ValueError:
      print("That's not even a number!")
      continue
    else:
      if menuChoice not in range(1, len(menuOptions) + 1):
        print("That's not an option!")
        continue

    return list(menuOptions.values())[menuChoice - 1]
