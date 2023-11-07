import random
import time

def rand_1d(size):

    result = []
    for i in range(size):
        result.append(random.randint(1, 100))
    return result 

def seq_1d(size):

    result = []
    for i in range(size):
        result.append(i)
    return result

def naive_peak_1d(array):

    counter = 1
    size = len(array) - 1

    if array == None:
        return 0, 0
    elif size == 1:
        return array[0], counter

    for i in range(1, size - 1):
        if array[i] > array[i - 1] and array [i] > array[i + 1]:
            return array[i], counter
        else:
            counter += 1

    return -1, counter

def divide_peak_1d(array, counter):

    size = len(array)
    mid = int(size/2) + 1

    if size < 3:
        return -1, counter
        
    if array[mid] < array[mid - 1]:
        half = array[0 : mid]
        return divide_peak_1d(half, counter + 1)
    elif array[mid] < array[mid + 1]:
        half = array[mid : size]
        return divide_peak_1d(half, counter + 1)
    else:
        return array[mid], counter

def main():
    size = input("lecture1_1dpeak.py\nPlease enter the size of the 1D array: ")

    worst_array = seq_1d(int(size))
    rand_array = rand_1d(int(size))

    if int(size) <= 100:
        print ("\nWorst Case Array:\n%s" % worst_array)
        print ("\nRandom Case Array:\n%s" % rand_array)
    
    start_time = time.time() * 1000
    print ("\nNaive Method, Worst Case n = " + size + ":\n")
    print (naive_peak_1d(worst_array))
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds" % (end_time - start_time))
    
    start_time = time.time() * 1000
    print ("\nDivide Method, Worst Case n = " + size + ":\n")
    print (divide_peak_1d(worst_array,1))
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds" % (end_time - start_time))
    
    start_time = time.time() * 1000
    print ("\nNaive Method, Random Case n = " + size + ":\n")
    print (naive_peak_1d(rand_array))
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds" % (end_time - start_time))
    
    start_time = time.time() * 1000
    print ("\nDivide Method, Random Case n = " + size + ":\n")
    print (divide_peak_1d(rand_array,1))
    end_time = time.time() * 1000
    print ("Time elapsed: %s milliseconds" % (end_time - start_time))
    input("Press return to exit...")
    
main()
