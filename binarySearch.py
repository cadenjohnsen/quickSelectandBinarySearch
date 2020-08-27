#!/usr/bin/env python3
from random import randint

# function to execute the binary search algorithm
def binarysearch(num, array):
    row = 0                     # start at the top
    col = int(len(array[0])) - 1   # start at the far right

    while((row < int(len(array))) and (col >= 0)):  # search from top right to bottom left
        if (num == array[row][col]):    # check if num is at that position
            return row, col    # answer found
        if (num < array[row][col]):
            col-=1  # go left
        else:
            row+=1  # go down
    return -10, -10     # return an impossible answer

# function to create a randomly sized 2D array in numerical order
def createRandomArray():
    array = []      # define empty array
    i, j = 0, 0
    k = 0
    num = randint(0, 10)    # number to be searched for in array
    m = randint(1,5)    # width of array
    n = randint(1, 5)   # length of array
    rows, cols = (n, m) # set rows and cols values
    result = -5     # set default as impossible value
    result2 = -5    # set default as impossible value

    for i in range(cols):   # loop through array adding random values
        temp = []    # declare temp array
        for j in range(rows):
            temp.append(k)  # add the new k value into the temp array
            k += 1          # increment k by 1
        array.append(temp)  # add the new number onto the final array
    return num, array

# function to call and execute other functions
def main():
    num, array = createRandomArray()
    result, result2 = binarysearch(num, array)

    print ("num:", num)     # prints the number being searched for
    print ("array:", array) # prints the array that was created
    if ((result >= 0) or (result2 >= 0)):   # check if a logical result location was found
        print ("(",result, ",", result2, ")")   # print the location
    else:   # the answer is not possible
        print ("Not Found")     # print that it does not exist

# beginning of the program to call main and start execution
if __name__ == "__main__":
	main()
