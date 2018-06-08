import unittest

import twisty_trampolines


class TwistyTrampolinesTest(unittest.TestCase):
    def test_num_exits_is_5_for_test_input(self):
        self.assertEquals(5, twisty_trampolines.steps_to_reach_exit('test_input.txt'))

    def test_num_exits_stranger_is_10_for_test_input(self):
        self.assertEqual(10, twisty_trampolines.steps_to_reach_exit_part_2('test_input.txt'))


if __name__ == '__main__':
    unittest.main()