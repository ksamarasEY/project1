import unittest
from app import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(-1,-1), -2)

    def test_greet(self):
        self.assertEqual(greet(),"Hello!")
        self.assertNotEqual(greet(), "")

if __name__ == "__main__":
    unittest.main()
