import unittest
from control import Home

class TestHome(unittest.TestCase):

    def test_home(self):
        result = Home.home()
        self.assertIsNone(result)


if __name__=='__main__':
    unittest.main()
