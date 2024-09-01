import unittest
import sys
import os

from scrap import scrap_pokemon

class TestScrap(unittest.TestCase):

    def test_fetch_data_bulbasaur(self):
        expected = [0]
        bulbasaurData = ""
        bulbasaurData += "1\n"
        bulbasaurData += "Bulbasaur\n"
        bulbasaurData += "Grass|Poison\n"
        bulbasaurData += "A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.\n"
        bulbasaurData += "1. Overgrow|Chlorophyll (hidden ability)\n"
        bulbasaurData += "45|49|49|65|65|45\n"
        bulbasaurData += "https://img.pokemondb.net/artwork/large/bulbasaur.jpg"
        expected[0] = bulbasaurData

        result = scrap_pokemon(1, 0)
        self.assertEqual(expected, result)

    def test_fetch_data_bulbasaur_line(self):
        expected = [0] * 3
        bulbasaurData = ""
        bulbasaurData += "1\n"
        bulbasaurData += "Bulbasaur\n"
        bulbasaurData += "Grass|Poison\n"
        bulbasaurData += "A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.\n"
        bulbasaurData += "1. Overgrow|Chlorophyll (hidden ability)\n"
        bulbasaurData += "45|49|49|65|65|45\n"
        bulbasaurData += "https://img.pokemondb.net/artwork/large/bulbasaur.jpg"
        expected[0] = bulbasaurData

        ivysaurData = ""
        ivysaurData += "2\n"
        ivysaurData += "Ivysaur\n"
        ivysaurData += "Grass|Poison\n"
        ivysaurData += "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.\n"
        ivysaurData += "1. Overgrow|Chlorophyll (hidden ability)\n"
        ivysaurData += "60|62|63|80|80|60\n"
        ivysaurData += "https://img.pokemondb.net/artwork/large/ivysaur.jpg"
        expected[1] = ivysaurData

        venusaurData = ""
        venusaurData += "3\n"
        venusaurData += "Venusaur\n"
        venusaurData += "Grass|Poison\n"
        venusaurData += "The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.\n"
        venusaurData += "1. Overgrow|Chlorophyll (hidden ability)\n"
        venusaurData += "80|82|83|100|100|80\n"
        venusaurData += "https://img.pokemondb.net/artwork/large/venusaur.jpg"
        expected[2] = venusaurData
        
        result = scrap_pokemon(3, 0)
        self.assertEqual(expected, result)
    
    def test_fetch_151_pokemon_save(self):
        result = scrap_pokemon(151, 1);
        self.assertEqual(151, len(result))

if __name__ == '__main__':
    unittest.main()
