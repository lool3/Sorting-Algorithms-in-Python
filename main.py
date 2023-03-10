import menu, sortmylist
import random, time

def main():
  randy = [random.randrange(1, 11) for x in range(10)]
  result = menu.menu({
    "Bubble sort": sortmylist.bubble(randy),
    "Selection sort": sortmylist.selection(randy),
    "Insertion sort": sortmylist.insertion(randy),
    "Quick sort": sortmylist.quick(randy)
  })
  print(result)

main()
