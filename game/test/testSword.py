import unittest
from sword import Sword


class TestSword(unittest.TestCase):
    def test_get_damage(self):
        self.assertEqual(Sword('Sw1', 10, 0.5).get_damage(), 5)
        self.assertEqual(Sword('Sw2', 100, 0.7).get_damage(), 70)
        self.assertEqual(Sword('Sw3', 40, 0.3).get_damage(), 12)

    def test_deal_damage(self):
        sw1 = Sword('StrongSword', 100, 1)
        sw1.deal_damage(r=1)
        self.assertTrue(sw1.durability == 0.9)
        sw1.deal_damage(r=0)
        self.assertTrue(sw1.durability == 0.9)

    def test_setter(self):
        sw = Sword('Sword', 0, 0)
        sw.name = 'Owowsword'
        sw.damage = 1
        sw.durability = 1
        self.assertFalse(sw.name == 'Sword')
        self.assertFalse(sw.damage == 0)
        self.assertFalse(sw.durability == 0)

    def test_getter(self):
        sw = Sword('Bow', 0, 0)
        self.assertTrue(sw.name == 'Bow')
        self.assertTrue(sw.damage == 0)
        self.assertTrue(sw.durability == 0)


if __name__ == '__main__':
    unittest.main()
