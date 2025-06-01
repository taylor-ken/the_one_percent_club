import unittest

from setup import get_contestants

class TestSetup(unittest.TestCase):
    def test_eq(self):
        # test empty folder
        dir_test_path = "./test_play_folders/test_play_1"
        contestants1 = get_contestants(dir_test_path)
        contestants2 = []
        self.assertEqual(contestants1, contestants2)

    def test_not_eq(self):
        dir_test_path_1 = "./test_play_folders/test_play_1"
        dir_test_path_2 = "./test_play_folders/test_play_2"
        a = get_contestants(dir_test_path_1)
        b = get_contestants(dir_test_path_2)
        self.assertNotEqual(a, b)

    def test_not_eq2(self):
        dir_test_path_1 = "./test_play_folders/test_play_2"
        dir_test_path_2 = "./test_play_folders/test_play_3"
        a = get_contestants(dir_test_path_1)
        b = get_contestants(dir_test_path_2)
        self.assertNotEqual(a, b)

if __name__ == "__main__":
    unittest.main()