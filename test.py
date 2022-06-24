import unittest
import main
class TestCat(unittest.TestCase):
    def test_voice(self):
        expected = "Meow"
        actual = main.Cat().voice()
        self.assertEqual(expected, actual)
class TestDog(unittest.TestCase):
    def test_voice(self):
        expected = "Gaw"
        actual = main.Dog().voice()
        self.assertEqual(expected, actual)
class TestFrog(unittest.TestCase):
    def test_voice(self):
        expected = "Kwa"
        actual = main.Frog().voice()
        self.assertEqual(expected, actual)
class TestWolf(unittest.TestCase):
    def test_voice(self):
        expected = "Auu"
        actual = main.Wolf().voice()
        self.assertEqual(expected, actual)