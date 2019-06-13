import unittest
import example

class WorkingExmapleTests(unittest.TestCase):

    # area(a, b)
    def test_area(self):
        self.assertEqual(example.area(5, 5), 25, "Should be 25")

    # area(a, b)
    def test_area_two(self):
        assert example.area(2, 3) == 6

    # full_name(a, b)
    def test_full_name(self):
        self.assertIsInstance(example.full_name("Keanu", "Reeves"), str)

if __name__ == '__main__':
    unittest.main()