import unittest

from change_dp import get_change

class TestGetChange(unittest.TestCase):
    def test_get_change(self):
        self.assertEqual(get_change(2),2)
        self.assertEqual(get_change(34), 9)
        self.assertEqual(get_change(1),1)
        self.assertEqual(get_change(5),2)

if __name__ == '__main__':
    unittest.main()