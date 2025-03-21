import unittest
from src import Fahrrad


class TestFahrrad(unittest.TestCase):
    def test_berechne_kosten(self):
        fahrrad = Fahrrad(strecke=20, koerpergewicht=70, skill_level=2)
        kalorien, kosten, reisezeit, doener = fahrrad.berechne_kosten()
        self.assertAlmostEqual(kosten, 5.76, places=2)


if __name__ == '__main__':
    unittest.main()
