import unittest


class EvenNumberTest(unittest.TestCase):

    def test_par(self):
        self.assertTrue(par(0))
        self.assertFalse(par(1))
        # self.assertTrue(par(2))
        # self.assertTrue(par(4))
        # self.assertTrue(par(42))

if __name__ == '__main__':
    unittest.main()
