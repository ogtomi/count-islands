import unittest
import count_islands

class TestCountIslands (unittest.TestCase):
    def setUp(self):
        self.arr = ['000000000', '010000000', '111000100', '110001110', '000001100', '001000000', '110000000', '000001100']
        self.rows = len(self.arr)
        self.cols = len(self.arr[0])
        self.counter = 4

    def test_get_2d(self):
        array = count_islands.get_2d(self.arr, self.rows, self.cols)
        self.assertTrue(type(array) is list)

    def test_count_islands(self):
        result = count_islands.count_islands(self.arr)
        self.assertEqual(result, self.counter)

if __name__ == '__main__':
    unittest.main()