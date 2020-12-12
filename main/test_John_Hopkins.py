import unittest
# from unittest.mock import patch
from John_Hopkins_COVID19 import *

class TestSirModel(unittest.TestCase):
    
    def setUp(self):
        self.value1 = sir(1000, 10, [2,3,4], 5, 7)
        self.value2 = sir(1000, 10, [2,3,4], 5, 7)._deriv(1,2,3,[10,20,30,40,50],5)
    


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)