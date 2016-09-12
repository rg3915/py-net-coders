import unittest


def par(n):
    return n % 2 == 0


class EvenNumberTest(unittest.TestCase):

    def test_0(self):
        self.assertEqual(par(0), True)

    def test_1(self):
        self.assertEqual(par(1), False)

    def test_42(self):
        self.assertEqual(par(42), True)


if __name__ == '__main__':
    unittest.main()
