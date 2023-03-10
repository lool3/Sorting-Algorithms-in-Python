import menu, sortmylist
import random, time

def main():
  randy = [random.randrange(1, 11) for x in range(10)]
  result = menu.menu({
    "Bubble sort": sortmylist.bubble,
    "Selection sort": sortmylist.selection,
    "Insertion sort": sortmylist.insertion,
    "Quick sort": sortmylist.quick
  })
  print(result(randy))

main()
