import unittest
# import import_ipynb
# from unittest.mock import patch
import importlib  
disease_spread = importlib.import_module("disease-spread")

class TestSirModel(unittest.TestCase):
    
    
    
    def test_Prb_IngPlane(self):
        self.assertEqual(disease_spread.probability_of_infected_plane(2/4), 0.5)
    

        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)