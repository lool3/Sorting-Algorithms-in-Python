# All algorithms sort smallest to largest
def bubble(sortme):
  while True:
    swapped = False
    for i in range(0, len(sortme) - 1):  # For each item except last
      if sortme[i] > sortme[i + 1]:  # If item on left > right
        sortme[i], sortme[i + 1] = sortme[i + 1], sortme[i]  #Swap
        swapped = True
    if swapped == False:  #If entire pass completed with no swaps
      return sortme

def selection(sortme):
  length = len(sortme)
  for i in range(length):
    minPointer = i
    for i2 in range(i + 1, length):  # For each index AFTER the pointer
      if sortme[i2] < sortme[
          minPointer]:  # If index is smaller than minimum pointer
        minPointer = i2  # Index is new minimum pointer
    sortme[i], sortme[minPointer] = sortme[minPointer], sortme[i]
  return sortme

def insertion(sortme):
  for i in range(1, len(sortme)):  # For each index excluding [0]
    p = i
    while sortme[p] < sortme[p - 1] and p > 0:  # If item on right < left
      sortme[p], sortme[p - 1] = sortme[p - 1], sortme[p]  # Swap
      p -= 1
  return sortme

def quick(sortme):
  if len(sortme) < 1: #No sorting required
    return sortme
  else:
    pivot = sortme.pop()
    higher = []
    lower = []
    for item in sortme:
      if item > pivot:
        higher.append(item)
      else:
        lower.append(item)
    return quick(lower) + [pivot] + quick(higher)

def merge(sortme):
  return f"I couldn't be bothered to sort the following list: {sortme}"

def counting(sortme):
  return f"I couldn't be bothered to sort the following list: {sortme}"

def radix(sortme):
  return f"I couldn't be bothered to sort the following list: {sortme}"

def bucket(sortme):
  return f"I couldn't be bothered to sort the following list: {sortme}"

def comb(sortme):
  return f"I couldn't be bothered to sort the following list: {sortme}"
