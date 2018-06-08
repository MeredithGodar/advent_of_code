import unittest

import spiral_memory


class SpiralMemoryTest(unittest.TestCase):
    def test_spiral_memory_of_1_is_0(self):
        self.assertEquals(0, spiral_memory.spiral_memory(1))

    def test_spiral_memory_of_12_is_3(self):
        self.assertEquals(3, spiral_memory.spiral_memory(12))

    def test_spiral_memory_of_23_is_2(self):
        self.assertEquals(2, spiral_memory.spiral_memory(23))

    def test_spiral_memory_of_1024_is_31(self):
        self.assertEquals(31, spiral_memory.spiral_memory(1024))

    def test_next_largest_value_of_1_is_2(self):
        self.assertEquals(2, spiral_memory.next_largest_value(1))

    def test_next_largest_value_of_2_is_4(self):
        self.assertEquals(4, spiral_memory.next_largest_value(2))

    def test_next_largest_value_of_23_is_25(self):
        self.assertEquals(25, spiral_memory.next_largest_value(23))


if __name__ == '__main__':
    unittest.main()
