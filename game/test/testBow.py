import unittest
from bow import Bow


class TestBow(unittest.TestCase):
    def test_get_damage(self):
        self.assertEqual(Bow('Bow1', 15, 0.5).get_damage(), 7.5)
        self.assertEqual(Bow('Bow2', 100, 0.7).get_damage(), 70)
        self.assertEqual(Bow('Bow3', 40, 0.3).get_damage(), 12)

    def test_deal_damage(self):
        bow1 = Bow('TrueShot', 100, 1)
        bow2 = Bow('WeakShot', 100, 0.2)
        self.assertTrue(bow1.deal_damage() == 100)
        self.assertTrue(bow1.deal_damage(r=0) == 100)
        self.assertTrue(bow2.deal_damage(r=1) == 0)
        self.assertTrue(bow2.deal_damage(r=0.1) == 100)

    def test_setter(self):
        bow = Bow('Bow1', 0, 0)
        bow.name = 'Bobo1'
        bow.damage = 1
        bow.accuracy = 1
        self.assertFalse(bow.name == 'Bow1')
        self.assertFalse(bow.damage == 0)
        self.assertFalse(bow.accuracy == 0)

    def test_getter(self):
        bow = Bow('Bow', 0, 0)
        self.assertTrue(bow.name == 'Bow')
        self.assertTrue(bow.damage == 0)
        self.assertTrue(bow.accuracy == 0)


if __name__ == '__main__':
    unittest.main()
