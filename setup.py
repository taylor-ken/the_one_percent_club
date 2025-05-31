import glob
from classes import Contestant, Game, Question
import random

def get_contestants(dir_path_play):
    contestants = []
    players_on_path = glob.glob(dir_path_play + "/*.txt")
    for player in players_on_path:
        name = player.rsplit('/',1)
        contestants.append(Contestant(name[-1]))
    return contestants

def generate_game(dir_path_questions, contestants):
    game = Game()
    game.playing_count = len(contestants)
    game.contestants = contestants
    rounds = ['90*', '80', '70', '60', '50', '45', '40', '35', '30', '25', '20', '15', '10', '05', '01']
    for round in rounds:
        options = glob.glob(dir_path_questions + "/" + round + "/*")
        game.questions.append(random.choice(options))
    return game
    