import unittest
from Shooter import Shooter


class TestFind(unittest.TestCase):

    def test1(self):
        shooter = Shooter()
        shooter.set_gun_by_name('Submachine Gun')
        shooter.add_bullet_of_given_size_to_gun(0.5, 1)
        self.assertEqual(shooter.shoot_to_target(1, 1, 20, 5, 4), 10)


if __name__ == '__main__':
    unittest.main()
