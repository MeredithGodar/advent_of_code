import unittest

import inverse_captcha


class InverseCaptchaTest(unittest.TestCase):
    def test_inverse_captcha_of_1122_is_3(self):
        self.assertEquals(3, inverse_captcha.inverse_captcha(1122))

    def test_inverse_captcha_of_1111_is_4(self):
        self.assertEquals(4, inverse_captcha.inverse_captcha(1111))

    def test_inverse_captcha_of_1234_is_0(self):
        self.assertEquals(0, inverse_captcha.inverse_captcha(1234))

    def test_inverse_captcha_of_91212129_is_9(self):
        self.assertEquals(9, inverse_captcha.inverse_captcha(91212129))

    def test_halfway_captcha_of_1212_is_6(self):
        self.assertEquals(6, inverse_captcha.halfway_captcha(1212))

    def test_halfway_captcha_of_1221_is_0(self):
        self.assertEquals(0, inverse_captcha.halfway_captcha(1221))

    def test_halfway_captcha_of_123425_is_4(self):
        self.assertEquals(4, inverse_captcha.halfway_captcha(123425))

    def test_halfway_captcha_of_123123_is_12(self):
        self.assertEquals(12, inverse_captcha.halfway_captcha(123123))

    def test_halfway_captcha_of_12131415_is_4(self):
        self.assertEquals(4, inverse_captcha.halfway_captcha(12131415))


if __name__ == '__main__':
    unittest.main()
