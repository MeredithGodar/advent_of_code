import unittest

import corruption_checksum


class CorruptionChecksumTest(unittest.TestCase):
    def test_corruption_checksum_of_test_input_part1_is_18(self):
        self.assertEquals(18, corruption_checksum.corruption_checksum('test_input_part1.csv'))

    def test_evenly_divisible_corruption_checksum_of_test_input_part2_is_18(self):
        self.assertEquals(9, corruption_checksum.evenly_divisible_corruption_checksum('test_input_part2.csv'))


if __name__ == '__main__':
    unittest.main()
