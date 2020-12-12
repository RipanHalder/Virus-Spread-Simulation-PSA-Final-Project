import unittest
# from unittest.mock import patch
from sir_model import SusInfRec as sir

class TestSirModel(unittest.TestCase):
    
    def setUp(self):
        self.value1 = sir(1000, 10, [2,3,4], 5, 7)
        self.value2 = sir(1000, 10, [2,3,4], 5, 7)._compute([7,8,9],2,3,[10,20,30,40,50],5)
    
#     def test_value(self):
#         self.assertEqual(self.value1.value(), 1024)
    
    def test_values(self):
        self.assertEqual(self.value1.N, 1000)
        self.assertEqual(self.value1.I0, 10)
        self.assertEqual(self.value1.b, [2,3,4])
        self.assertEqual(self.value1.k, 5)
        self.assertIsNotNone(self.value1.S0) 
        self.assertEqual(self.value1.days, 7)
        
    def test_compute(self):
        self.test_compute = self.value1._compute([7,8,9],2,3,[10,20,30,40,50],5)
        self.assertIsNotNone(self.test_compute[0])
        self.assertIsNotNone(self.test_compute[1])
        self.assertIsNotNone(self.test_compute[2])  
    
#     def test_run(self):
#         self.value2 = sir(1000, 10, 2, 5, 7)
# #         output = self.value2._deriv(1,2,3,[10,20,30,40,50],5)
#         self.assertTrue(self.value2.run())
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)