import math


# http://adventofcode.com/2017/day/3


# Part 1:

# You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

# Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up
# while spiraling outward. For example, the first few squares are allocated like this:

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

# While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1
# (the location of the only access port for this memory system) by programs that can only move up, down, left,
# or right. They always take the shortest path: the Manhattan Distance (https://en.wikipedia.org/wiki/Taxicab_geometry)
# between the location of the data and square 1.

# For example:

#     Data from square 1 is carried 0 steps, since it's at the access port.
#     Data from square 12 is carried 3 steps, such as: down, left, left.
#     Data from square 23 is carried only 2 steps: up twice.
#     Data from square 1024 must be carried 31 steps.

# How many steps are required to carry the data from the square identified in your puzzle input all the way
# to the access port?

# Your puzzle input is 361527.


# Part 2:

# As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1.
# Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares,
# including diagonals.

# So, the first few squares' values are chosen as follows:

#     Square 1 starts with the value 1.
#     Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
#     Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
#     Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
#     Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

# Once a square is written, its value does not change.
# Therefore, the first few squares would receive the following values:

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...

# What is the first value written that is larger than your puzzle input?


def spiral_memory(input_num):
    if input_num == 1:
        return 0
    else:
        root = math.ceil(math.sqrt(input_num))

        side_length = root if root % 2 != 0 else root + 1

        distance_from_radicand_to_center = int((side_length - 1) / 2)

        next_smallest_radicand = (side_length - 2) ** 2

        side_length_of_next_smallest_square = side_length - 1

        offset_of_input_num_from_radicand = (input_num - next_smallest_radicand) % side_length_of_next_smallest_square

        offset_from_center = abs(offset_of_input_num_from_radicand - distance_from_radicand_to_center)

        manhattan_distance = int(distance_from_radicand_to_center + offset_from_center)

        # for an input_num of 23:

        # 17  16  15  14  13
        # 18   5   4   3  12
        # 19   6   1   2  11
        # 20   7   8   9  10  <-  9 is the radicand for the next smallest square
        # 21  22  23  24  25  <- 25 is the radicand for our root (5)

        # __________________  side_length = 5
        #          2___1___0  distance_from_radicand_to_center = 2
        #          0___1___2  offset_of_input_num_from_radicand = 2
        #          *          offset_from_center = 0

        # manhattan_distance = abs(offset_of_input_num_from_radicand - distance_from_radicand_to_center)
        #                    = abs(2 - 0)
        #                    = 2

        return manhattan_distance


def next_largest_value(input_num):
    # b141481.txt taken from: https://oeis.org/A141481

    with open('b141481.txt') as txt:
        for line in txt:
            if not line.startswith("#"):
                num_to_check = int(line.split()[1])
                if num_to_check > input_num:
                    return num_to_check


if __name__ == '__main__':

    my_input = 361527

    print("The spiral memory of %d is %d" % (my_input, spiral_memory(my_input)))
    print("The next largest value is %d" % next_largest_value(my_input))

