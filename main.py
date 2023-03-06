import sortmylist
import random, time
def main():
  print(
    "This program will sort a random list of integers from smallest to largest"
  )
  randomList = list(range(1000))  #Create array of random integers to sort
  random.shuffle(randomList)
  algorithms = {
    0: sortmylist.bubble,
    1: sortmylist.selection,
    2: sortmylist.insertion,
    3: sortmylist.quick,
    4: sortmylist.merge,
    5: sortmylist.counting,
    6: sortmylist.radix,
    7: sortmylist.bucket,
    8: sortmylist.comb
  }
  algorithm = choose()
  start = time.time()
  print(algorithms.get(algorithm)(randomList))
  print(f'Time taken in seconds: {time.time() - start}')
def choose():
  algorithms = ("BUBBLE", "SELECTION", "INSERTION", "QUICK", "MERGE",
                "COUNTING", "RADIX", "BUCKET", "COMB")
  for i, item in enumerate(algorithms):
    print(f"{i}. {item}")
  while True:
    try:
      choice = int(input("Pick a sorting algorithm: "))
      if choice < 0 or choice > len(algorithms) - 1:
        raise ValueError("Invalid choice")
      else:
        return choice
    except ValueError as err:
      print(f"Error: {err}. Try again...")
      continue
if __name__ == "__main__":
  main()
