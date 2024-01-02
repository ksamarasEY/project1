import unittest
from app import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(-1,-1), -2)

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
