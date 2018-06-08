import unittest

import high_entropy_passphrases


class HighEntropyPassphrasesTest(unittest.TestCase):
    def test_valid_passphrases_is_2_for_test_input_part_1(self):
        self.assertEquals(2, high_entropy_passphrases.count_valid_passphrases('test_input_part_1.txt'))

    def test_valid_passphrases_no_anagrams_is_3_for_test_input_part_2(self):
        self.assertEquals(3, high_entropy_passphrases.count_valid_passphrases_no_anagrams('test_input_part_2.txt'))


if __name__ == '__main__':
    unittest.main()