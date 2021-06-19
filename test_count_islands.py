import unittest
import count_islands

class TestCountIslands (unittest.TestCase):
    def setUp(self):
        self.arr_2d = ['000000000', '010000000', '111000100', '110001110', '000001100']
        self.rows = len(self.arr_2d)
        self.cols = len(self.arr_2d[0])

    def test_get_2d(self):
        array = count_islands.get_2d(self.arr_2d, self.rows, self.cols)
        self.assertTrue(type(array) is list)

if __name__ == '__main__':
    unittest.main()