import random
import time

counter = 0

def rand_1d(size):

  result = []
  for i in range(size):
    result.append(random.randint(1, 100))
  return result

def combine(array_a, array_b):

  global counter
  for item in array_b:
    array_a.append(item)
    counter = counter + 1
  return array_a

def merge_sort(array):

  global counter
  counter = counter + 1
  length = len(array)
  result = []
  if length > 2:
    left = merge_sort(array[0:int(length/2)])
    right = merge_sort(array[int(length/2):length])
    for i in range(length):
      if len(left) == 0:
        result = combine(result, right)
        break
      elif len(right) == 0:
        result = combine(result, left)
        break
      elif left[0] < right[0]:
        result.append(left.pop(0))
      else:
        result.append(right.pop(0))
    return result
  elif length == 2:
    if array[0] > array[1]:
      temp = array[0]
      array[0] = array[1]
      array[1] = temp
    result = array
    return result
  else:
    return array

def main():
  size = input("lecture3_mergesort.py\nPlease enter the size of the 1D array: ")
  to_print = int(size) <= 500
  array_input = rand_1d(int(size))
  if to_print:
    print ("\n", array_input)
  start_time = time.time()
  array_output = merge_sort(array_input)
  end_time = time.time()
  print ("\nInput length n: %s\n\nNumber of operations: %s" % (len(array_input), counter))
  print ("\nTime elapsed: %s seconds" % (end_time - start_time))
  if to_print:
    print ("\n", array_output)
  input("Press return to exit...")

main()
