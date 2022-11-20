import sortmylist
import random, time


def main():
  print(
    "This program will sort a random list of integers from smallest to largest"
  )
  randomList = []  #Create array of random integers to sort
  for i in range(100):
    randomList.append(random.randrange(0, 1000))
    
  algorithms = {
    0:sortmylist.bubble(randomList),
    1:sortmylist.selection(randomList),
    2:sortmylist.insertion(randomList),
    3:sortmylist.quick(randomList),
    4:sortmylist.merge(randomList),
    5:sortmylist.counting(randomList),
    6:sortmylist.radix(randomList),
    7:sortmylist.bucket(randomList),
    8:sortmylist.comb(randomList)
  }
  algorithm = choose()
  
  start = time.time()
  print(algorithms.get(algorithm))
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
