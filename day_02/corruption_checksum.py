import csv

import sys


# http://adventofcode.com/2017/day/2

# Part 1:

# The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right
# track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the
# largest value and the smallest value; the checksum is the sum of all of these differences.

# For example, given the following spreadsheet:

# 5 1 9 5
# 7 5 3
# 2 4 6 8

#    The first row's largest and smallest values are 9 and 1, and their difference is 8.
#    The second row's largest and smallest values are 7 and 3, and their difference is 4.
#    The third row's difference is 6.

# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

# What is the checksum for the spreadsheet in your puzzle input?


# Part 2:

# It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is,
# where the result of the division operation is a whole number. They would like you to find those numbers on each line,
# divide them, and add up each line's result.

# For example, given the following spreadsheet:

# 5 9 2 8
# 9 4 7 3
# 3 8 6 5

#     In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
#     In the second row, the two numbers are 9 and 3; the result is 3.
#     In the third row, the result is 2.

# In this example, the sum of the results would be 4 + 3 + 2 = 9.

# What is the sum of each row's result in your puzzle input?


def corruption_checksum(filename):
    checksum = 0

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            max_val = 0
            min_val = sys.maxsize

            for val in row:
                val = int(val)
                if val >= max_val:
                    max_val = val
                if val <= min_val:
                    min_val = val

            checksum += abs(max_val - min_val)

    return checksum


def evenly_divisible_corruption_checksum(filename):
    checksum = 0

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            for i in range(0, len(row)):
                for j in range(i + 1, len(row)):
                    left = int(row[i])
                    right = int(row[j])

                    if left % right == 0:
                        checksum += int(left / right)
                        break
                    elif right % left == 0:
                        checksum += int(right / left)
                        break
    return checksum


if __name__ == '__main__':

    print("The corruption checksum is %d" % corruption_checksum('day_02_input.csv'))
    print("The evently divisible corruption checksum is %d" % evenly_divisible_corruption_checksum('day_02_input.csv'))
