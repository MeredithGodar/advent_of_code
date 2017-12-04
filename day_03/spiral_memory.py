import math


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


def adjacent_sum(input_num):
    return 1
