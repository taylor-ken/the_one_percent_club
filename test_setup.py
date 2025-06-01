import unittest

from setup import get_contestants

class TestSetup(unittest.TestCase):
    def test_eq(self):
        # test empty folder
        dir_test_path = "./test_play_folders/test_play_1"
        contestants1 = get_contestants(dir_test_path)
        contestants2 = []
        self.assertEqual(contestants1, contestants2)


if __name__ == "__main__":
    unittest.main()