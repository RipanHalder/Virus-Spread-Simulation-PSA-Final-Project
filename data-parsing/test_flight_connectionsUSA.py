import unittest
# import import_ipynb
import ipynb.fs.flight_connections_usa as usaFlight
# from unittest.mock import patch
# import disease_spread

class TestDiseaseSpread(unittest.TestCase):
    
    def test_population_link(self):
        self.assertIsNotNone(usaFlight.get_soup("https://www.flightconnections.com/airport-codes")) 
    
#     def test_Prb_InfPlane(self):
#         self.assertEqual(dis.probability_of_infected_plane(2,4), 0.5)
        
# #     def test_Prb_InfCity(self):
# #         self.assertIsNotNone(dis.probability_of_infected_city(10, 100, [5,6]))

#     def test_cityNeighbours(self):
#         self.assertIsNotNone(dis.find_neighbours_of_a_city("Boston"))
        
#     def test_healthy_airports(self):
#         self.assertIsNotNone(dis.find_all_current_healthy_airports(["BOS","NYC"]))
        
#     def test_infected_airports(self):
#         self.assertIsNotNone(dis.find_all_current_infected_airports(["BOS","NYC"]))
 
    
    
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)