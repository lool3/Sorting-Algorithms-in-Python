# All algorithms sort smallest to largest
def bubble(sortme):
  while True:
    swapped = False
    for i in range(0, len(sortme) - 1):
      if sortme[i] > sortme[i + 1]:  # If item on left > right
        sortme[i], sortme[i + 1] = sortme[i + 1], sortme[i]
        swapped = True
    if swapped == False:
      return (sortme)
def selection(sortme):
  return (f"I couldn't be bothered to sort the following list: {sortme}")  # TODO
def insertion(sortme):
  for i in range(1, len(sortme)):  # For each index excluding [0]
    p = i
    while sortme[p] < sortme[p - 1] and p > 0:  # If item on right < left
      sortme[p], sortme[p - 1] = sortme[p - 1], sortme[p]  # Swap
      p -= 1
  return (sortme)
def quick(sortme):
  return (f"I couldn't be bothered to sort the following list: {sortme}")  # TODO
def merge(sortme):
  return (f"I couldn't be bothered to sort the following list: {sortme}")  # TODO
def counting(sortme):
  return (f"I couldn't be bothered to sort the following list: {sortme}")  # TODO
def radix(sortme):
  return (f"I couldn't be bothered to sort the following list: {sortme}")  # TODO
def bucket(sortme):
  return (f"I couldn't be bothered to sort the following list: {sortme}")  # TODO
def comb(sortme):
  return (f"I couldn't be bothered to sort the following list: {sortme}")  # TODO
