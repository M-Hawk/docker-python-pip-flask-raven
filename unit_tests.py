import unittest
from classes import Player, ComputerPlayer, Game


# P2P TESTS
class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestPlayer", 120, "Tracked", "Flipper", 25)

    def test_getters(self):
        self.assertEqual(self.player.get_name(), "TestPlayer")
        self.assertEqual(self.player.get_health(), 120)
        self.assertEqual(self.player.get_body_type(), "Tracked")
        self.assertEqual(self.player.get_weapon(), "Flipper")

    def test_setters(self):
        self.player.set_name("NewName")
        self.assertEqual(self.player.get_name(), "NewName")

        self.player.set_age(30)  # no getter for age, so no assert here

        self.player.set_body_type("Soft-Wheeled")
        self.assertEqual(self.player.get_body_type(), "Soft-Wheeled")

        self.player.set_weapon("Powersaw")
        self.assertEqual(self.player.get_weapon(), "Powersaw")

    def test_damage(self):
        self.player.damage(20)
        self.assertEqual(self.player.get_health(), 100)


class TestComputerPlayer(unittest.TestCase):

    def test_computer_player_initialization(self):
        bot = ComputerPlayer()
        self.assertIn(bot.get_name(), ComputerPlayer.bot_names)
        self.assertIn(bot.get_body_type(), ComputerPlayer.bot_body_type)
        self.assertIn(bot.get_weapon(), ComputerPlayer.bot_weapon)
        self.assertEqual(bot.get_health(), 120)


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_weap_weap_dmg(self):
        self.assertEqual(self.game.weap_weap_dmg("Electrocutor", "Flipper"), 30)
        self.assertEqual(self.game.weap_weap_dmg("Electrocutor", "Electrocutor"), 10)
        self.assertEqual(self.game.weap_weap_dmg("Electrocutor", "Powersaw"), 20)

    def test_weap_body_dmg(self):
        self.assertEqual(self.game.weap_body_dmg("Electrocutor", "Tracked"), 30)
        self.assertEqual(self.game.weap_body_dmg("Electrocutor", "Soft-Wheeled"), 10)
        self.assertEqual(self.game.weap_body_dmg("Electrocutor", "Hard-Wheeled"), 20)

# F2P TESTS




# Runs when file is executed directly as above
if __name__ == '__main__':
    unittest.main()