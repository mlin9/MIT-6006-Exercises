import random
import time

def rand_1d(size):

  result = []
  for i in range(size):
    result.append(random.randint(1, 100))
  return result

def insertion_sort(array):

  to_print = len(array) <= 500

  if to_print:
    print ("\n", array)
    
  start_time = time.time()
  steps = 0
  length = len(array)
  for i in range(1, length):
    j = i
    if array[i] < array[i - 1]:
      while array[j] < array[j - 1] and j > 0:
        temp = array[j]
        array[j] = array[j - 1]
        array[j - 1] = temp
        j = j - 1
        steps = steps + 1
  end_time = time.time()
  print ("\nInput length n: %s" % length)
  print ("\nNumber of operations: %s" % steps)
  print ("\nTime elapsed: %s seconds" % (end_time - start_time))
  
  if to_print:
    print ("\n", array)

def main():
  size = input("lecture3_insertsort.py\nPlease enter the size of the 1D array: ")
  input_array = rand_1d(int(size))
  insertion_sort(input_array)
  input("Press return to exit...")

main()
