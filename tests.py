import unittest
import example

class WorkingExmapleTests(unittest.TestCase):
    def test_area(self):
        self.assertIsInstance (example.area(5, 5), int)

    def test_full_name(self):
        self.assertIsInstance (example.full_name("Keanu", "Reeves"), str)

if __name__ == '__main__':
    unittest.main()