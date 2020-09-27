import unittest
from view import Choose

class TestChoose(unittest.TestCase):

    def test_Choices(self):
        result = Choose.choices()
        self.assertIsNone(result)


if __name__=='__main__':
    unittest.main()
