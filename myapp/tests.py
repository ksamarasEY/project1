import unittest
import io
import sys
from app import add, greet, sub 

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(-1,-1), -2)

    def test_sub(self):
        self.assertEqual(sub(2,1), 1)
        self.assertEqual(sub(1,1), 0)
        self.assertEqual(sub(-1,-1), 0)

    def test_greet(self):
        # Capture the output of greet() using an io.StringIO object
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        greet()
        sys.stdout = sys.__stdout__

        # Check if "Hello!\n" was printed (note the newline character)
        self.assertEqual(capturedOutput.getvalue(), "Hello!\n")

if __name__ == "__main__":
    unittest.main()
