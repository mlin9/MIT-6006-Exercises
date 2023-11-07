import random
import time

array_2d = []
length_2d = 0

def printout(array):
    if len(array) > 10:
        return
    
    for row in array:
        for entry in row:
            print ("\t%s" % entry, end=""),
        print ()

def rand_1d(size):

    result = []
    for i in range(size):
        result.append(random.randint(1, 101))
    return result

def seq_1d(size, increment):

    result = []
    for i in range(size):
        result.append(i + increment)
    return result

def rand_2d(length):

    result = []
    for i in range(length):
        result.append(rand_1d(length))
    return result

def seq_2d(length):

    result = []
    for i in range(length):
        result.append(seq_1d(length, i))
    return result

def naive_peak_2d(array, counter):

    length = len(array[0]) - 1
    row = int(length / 2)
    col = int(length / 2)
    tracker = 0

    while True:
        tracker -= 1
        if row == length - 1 or col == length - 1 or row == 1 or col == 1:
            array[row][col] = '#'
            printout(array)
            return -1, counter
        elif array[row][col] <= array[row - 1][col - 1] and row - 1 > 1 and col - 1 > 1:
        #upleft
            if array[row - 1][col - 1] > 0:
                counter += 1
                row -= 1
                col -= 1
                array[row + 1][col + 1] = tracker
        elif array[row][col] <= array[row][col - 1] and col - 1 > 1:
        #up
            if array[row][col - 1] > 0:
                counter += 1
                col -= 1
                array[row][col + 1] = tracker
        elif array[row][col] <= array[row + 1][col - 1] and row + 1 < length and col - 1 > 1:
        #upright
            if array[row + 1][col - 1] > 0:
                counter += 1
                row += 1
                col -= 1
                array[row - 1][col + 1] = tracker
        elif array[row][col] <= array[row - 1][col] and row - 1 > 1:
        #left
            if array[row - 1][col] > 0:
                counter += 1
                row -= 1
                array[row + 1][col] = tracker
        elif array[row][col] <= array[row + 1][col] and row + 1 < length:
        #right
            if array[row + 1][col] > 0:
                counter += 1
                row += 1
                array[row - 1][col] = tracker
        elif array[row][col] <= array[row - 1][col + 1] and row - 1 > 1 and col + 1 < length:
        #downleft
            if array[row - 1][col + 1] > 0:
                counter += 1
                row -= 1
                col += 1
                array[row + 1][col - 1] = tracker
        elif array[row][col] <= array[row][col + 1] and col + 1 < length:
        #down
            if array[row][col + 1] > 0:
                counter += 1
                col += 1
                array[row][col - 1] = tracker
        elif array[row][col] <= array[row + 1][col + 1] and row + 1 < length and col + 1 < length:
        #downright
            if array[row + 1][col + 1] > 0:
                counter += 1
                row += 1
                col += 1
                array[row - 1][col - 1] = tracker
        else:
            value = array[row][col]
            array[row][col] = '#'
            printout(array)
            return value, counter

def divide_peak_1d(array, counter):

    size = len(array)
    mid = int(size/2)

    if size < 3:
        return -1, counter

    if array[mid] < array[mid - 1]:
        half = array[0 : mid]
        return divide_peak_1d(half, counter + 1)
    elif array[mid] < array[mid + 1]:
        half = array[mid : size]
        return divide_peak_1d(half, counter + 1)
    else:
        return mid, counter

def divide_peak_2d(array, col, counter):

    row, step = divide_peak_1d(array[col], counter)
    counter += step + 1

    if row < 1:
        row = int(length_2d / 2)

    if col - 1 > 0 and array[col][row] < array[col - 1][row]:
        array[col][row] = counter * -1
        return divide_peak_2d(array, col - 1, counter)
    elif col + 1 < length_2d - 1 and array[col][row] < array[col + 1][row]:
        array[col][row] = counter * -1
        return divide_peak_2d(array, col + 1, counter)
    elif array[col][row] > array[col - 1][row] and array[col][row] > array[col + 1][row]:
        value = array[row][col]
        array[row][col] = '#'
        printout(array)
        return value
    else:
        value = array[row][col]
        array[row][col] = '#'
        printout(array)
        return value

def main():
    size = input("lecture1_2dpeak.py\nPlease enter the side length of the 2D array: ")
    length_2d = int(size)
    to_print = length_2d <= 10

    seq_array = seq_2d(length_2d)

    if to_print:
        print ("Sequential array:\n")
        printout(seq_array)

    rand_array = rand_2d(length_2d)

    if to_print:
        print ("Random array:\n")
        printout(rand_array)

    start_time = time.time() * 1000
    print ("Naive Method, Sequential Case n = " + size + ":\n")
    print ("Result: Value = %s, Moves = %s\n" % naive_peak_2d(seq_array, 0))
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds\n" % (end_time - start_time))

    start_time = time.time() * 1000
    print ("Naive Method, Random Case n = " + size + ":\n")
    print ("Result: Value = %s, Moves = %s\n" % naive_peak_2d(rand_array, 0))
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds\n" % (end_time - start_time))

    start_time = time.time() * 1000
    print ("Divide Method, Sequential Case n = " + size + ":\n")
    print ("Result: Value = %s\n" % divide_peak_2d(seq_array, int(length_2d/2), 0))
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds\n" % (end_time - start_time))

    start_time = time.time() * 1000
    print ("Divide Method, Random Case n = " + size + ":\n")
    print ("Result: Value = %s\n" % divide_peak_2d(rand_array, int(length_2d/2), 0))
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds\n" % (end_time - start_time))
    input("Press return to exit...")

main()
