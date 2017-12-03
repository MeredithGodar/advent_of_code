import csv

import sys


def corruption_checksum(filename):
    checksum = 0

    with open(filename, newline='') as csvfile:
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

    with open(filename, newline='') as csvfile:
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
