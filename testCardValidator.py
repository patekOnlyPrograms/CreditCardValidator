import unittest

from CardValidator import luhnAlgorithm


class MyTestCase(unittest.TestCase):

    def test_luhnAlgorithm_With_Whitespaces(self):
        self.assertEqual(luhnAlgorithm("5555 5555 5555 4444"), True)

    def test_luhnAlgorithm_FailCase(self):
        self.assertFalse(luhnAlgorithm("799273987135"), False)

    def test_luhnAlgorithm_American_Express(self):
        self.assertEqual(luhnAlgorithm("378282246310005"), True)

    def test_luhnAlgorithm_American_Express_Corporate(self):
        self.assertEqual(luhnAlgorithm("378734493671000"), True)

if __name__ == '__main__':
    unittest.main()
