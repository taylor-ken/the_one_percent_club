import unittest

from src.play_game import display_question, answer_checker
from src.setup import get_contestants, generate_game

class TestDisplayQuestion(unittest.TestCase):
    def test_eq(self):
        sample_question = "Which of these photographs has to be wrong?"
        dir_path_questions = "./questions"
        question_link = "./questions/90/s01e01.json"
        current_question = display_question(dir_path_questions, question_link)
        self.assertEqual(sample_question, current_question.question)

class TestAnswerChecker(unittest.TestCase):
    def test_eq(self):
        dir_test_path_2 = "./test/test_play_folders/test_play_2"
        dir_path_questions = "./questions"
        contestants = get_contestants(dir_test_path_2)
        game = generate_game(dir_path_questions, contestants)
        question_link = "./questions/90/s01e01.json"
        current_question = display_question(dir_path_questions, question_link)

        game = answer_checker(game, dir_test_path_2, current_question)
        self.assertTrue(game.contestants[1].is_eliminated)

if __name__ == "__main__":
    unittest.main()