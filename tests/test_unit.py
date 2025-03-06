import unittest
from main import Auto


class TestAuto(unittest.TestCase):
    def test_berechne_kosten(self):
        # Beispiel: Auto fährt 100 km, 1 Stunde, Spritkosten 1.50, Verbrauch 7 l/100km
        auto = Auto(100, 1, 1.50, 7)
        kosten = auto.berechne_kosten()
        # Erwarteter Wert: (100 / 100) * 7 * 1.50 = 10.5
        self.assertAlmostEqual(kosten, 10.5)
