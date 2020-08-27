#!/usr/bin/env python3
from random import randint

# function to shift around the array to be used easier
def partition(array, pivot, left, right):
    x = array[right]    # set the last value into a variable
    i = left    # start i at the first value
    for j in range (left, right):
        if (array[j] <= x): # checks if the array at current index is less than the right
            array[i], array[j] = array[j], array[i]     # swap the indexes
            i += 1  # increment left value
    array[i], array[right] = array[right], array[i]     # swap right value into the correct position
    return i    # return the position to become the pivot

# function to execute the quick select algorithm
def quick_select(k, array):
    def find_kth_smallest(k, array, left, right):   # sub function to include left and right
        if (left == right):     # checks if you are at the exact last possible position
            return array[left]      # if at correct index then return the answer
        pivot = randint(left, right - 1)    # enter a random number for the pivot within the range
        pivot = partition(array, pivot, left, right)    # call the partition function to shift the array
        if (k == pivot):        # check if the wanted number is found
            return array[k]     # return answer
        elif (k < pivot):   # check if k is lower than the pivot
            return find_kth_smallest(k, array, left, pivot - 1)     # shift the array one from the right and iterate
        else:       # checks if k is higher than the pivot
            return find_kth_smallest(k, array, pivot + 1, right)    # shift the array one from the left and iterate
    return find_kth_smallest(k, array, 0, len(array)-1)     # calls the sub function and returns its value

# function to create an array of random size with random variables
def createRandomArray():
    array = []		# declare the initially empty  array
    i, k = 0, 0
    temp = 0
    n = randint(1, 10)   # select a random number of variables to determine array length
    k = randint(0, n - 1)   # position to be looked for in the array: kth smallest value

    for i in range(0, n):
        temp = randint(0,100)
        array.append(temp)  # add the new random number onto the array

    return k, array    # return the created array and the position to be searched for

# function to call and execute other functions
def main():
    k, array = createRandomArray()
    num = quick_select(k, array)

    k += 1  # increment k value to make the printing seem more user friendly
    print("kth smallest:    ", k)       # print the value of k that is search for
    print("array:           ", array)   # print the final array
    print("num:             ", num)      # print the number found

# beginning of the program to call main and start execution
if __name__ == "__main__":
	main()
