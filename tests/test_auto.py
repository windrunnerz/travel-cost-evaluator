import unittest
from src import Auto


class TestAuto(unittest.TestCase):
    def test_berechne_kosten(self):
        auto = Auto(strecke=100, reisezeit=1, spritkosten=1.50, verbrauch=7)
        kosten = auto.berechne_kosten()
        self.assertEqual(kosten, 10.5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
