import unittest

from src.setup import get_contestants, generate_game

class TestGetContestants(unittest.TestCase):
    def test_eq(self):
        # test empty folder
        dir_test_path = "./test_play_folders/test_play_1"
        contestants1 = get_contestants(dir_test_path)
        contestants2 = []
        self.assertEqual(contestants1, contestants2)

    def test_not_eq(self):
        dir_test_path_1 = "./test/test_play_folders/test_play_1"
        dir_test_path_2 = "./test/test_play_folders/test_play_2"
        a = get_contestants(dir_test_path_1)
        b = get_contestants(dir_test_path_2)
        self.assertNotEqual(a, b)

    def test_not_eq2(self):
        dir_test_path_1 = "./test/test_play_folders/test_play_2"
        dir_test_path_2 = "./test/test_play_folders/test_play_3"
        a = get_contestants(dir_test_path_1)
        b = get_contestants(dir_test_path_2)
        self.assertNotEqual(a, b)

    def test_load(self):
        dir_test_path = "./test/test_play_folders/test_play_2"
        contestants1 = get_contestants(dir_test_path)
        
        self.assertEqual(len(contestants1), 4)

class TestGenerateGame(unittest.TestCase):
    def test_questions(self):
        dir_path_questions = "./questions"
        game = generate_game(dir_path_questions, [])
        # check that we get 15 questions
        self.assertEqual(len(game.questions), 15)

    def test_questions_are_random(self):
        dir_path_questions = "./questions"
        game1 = generate_game(dir_path_questions, [])
        game2 = generate_game(dir_path_questions, [])
        self.assertNotEqual(game1.questions, game2.questions)

if __name__ == "__main__":
    unittest.main()