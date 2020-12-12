import unittest
# import import_ipynb
from ipynb.fs.full.US_Cities_Population import get_soup
# from unittest.mock import patch
# import disease_spread

class TestDiseaseSpread(unittest.TestCase):
    
    def test_population_link(self):
        self.assertIsNotNone(get_soup("http://worldpopulationreview.com/us-cities/")) 
    
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)