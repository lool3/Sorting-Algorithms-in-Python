import sortmylist
import random, time


def main():
  print(
    "This program will sort a random list of integers from smallest to largest"
  )
  algorithm = choose()

  randomList = []  #Create array of random integers to sort
  for i in range(100):
    randomList.append(random.randrange(0, 1000))
  start = time.time()
  if algorithm == 0:
    print(sortmylist.bubble(randomList))
  elif algorithm == 1:
    print(sortmylist.selection(randomList))
  elif algorithm == 2:
    print(sortmylist.insertion(randomList))
  elif algorithm == 3:
    print(sortmylist.quick(randomList))
  elif algorithm == 4:
    print(sortmylist.merge(randomList))
  elif algorithm == 5:
    print(sortmylist.counting(randomList))
  elif algorithm == 6:
    print(sortmylist.radix(randomList))
  elif algorithm == 7:
    print(sortmylist.bucket(randomList))
  elif algorithm == 8:
    print(sortmylist.comb(randomList))
  print(f'Time taken in seconds: {time.time() - start}')


def choose():
  algorithms = ("BUBBLE", "SELECTION", "INSERTION", "QUICK", "MERGE",
                "COUNTING", "RADIX", "BUCKET", "COMB")
  for i, item in enumerate(algorithms):
    print(f"{i}. {item}")

  while True:
    try:
      choice = int(input("Pick a sorting algorithm: "))
      if choice < 0 or choice > len(algorithms):
        raise ValueError("Invalid choice")
      else:
        return choice
    except ValueError as err:
      print(f"Error: {err}. Try again...")
      continue


if __name__ == "__main__":
  main()
