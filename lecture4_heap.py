import random
import time

valid = True
counter = 0

def rand_1d(size):
    result = ['Begin:']
    for i in range(size):
        result.append(random.randint(1, 100))
    return result

def max_heap(array, pos):

    global counter
    counter = counter + 1
    length = len(array)
    left = 2 * pos
    right = 2 * pos + 1
    if left >= length or right >= length:
        return
    elif array[pos] > array[left] and array[pos] > array[right]:
        return
    elif array[left] > array[right]:
        temp = array[pos]
        array[pos] = array[left]
        array[left] = temp
        max_heap(array, left)
    else:
        temp = array[pos]
        array[pos] = array[right]
        array[right] = temp
        max_heap(array, right)

def build_max_heap(array):

    length = len(array)
    for i in range(int(length / 2), 0, -1):
        max_heap(array, i)

def test_heap(array, pos):

    global valid
    length = len(array)
    left = 2 * pos
    right = 2 * pos + 1
    if left >= length or right >= length:
        return
    elif array[pos] < array[left] or array[pos] < array[right]:
        print ("\nInvalid heap!")
        valid = False
    else:
        test_heap(array, left)
        test_heap(array, right)

def verify_max_heap(array):

    length = len(array)
    for i in range(int(length / 2), 0, -1):
        test_heap(array, i)

def main():
    global counter
    size = input("lecture4_heap.py\nPlease enter the size of the 1D array: ")
    to_print = int(size) <= 500
    input_array = rand_1d(int(size))
    if to_print:
        print ("\n", input_array)
    start_time = time.time() * 1000
    build_max_heap(input_array)
    end_time = time.time() * 1000
    verify_max_heap(input_array)

    if to_print:
        print ("\n", input_array)

    if valid:
        print ("\nValid heap!")

    print ("\nInput length n: %s\n\nNumber of operations: %s" % (int(size), counter))
    print ("\nTime elapsed: %s milliseconds" % (end_time - start_time))
    input("Press return to exit...")

main()
