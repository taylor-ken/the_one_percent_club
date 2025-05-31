from pathlib import Path
from classes import Game, Question
from setup import get_contestants, generate_game
from play_game import play_game
from dataclasses import dataclass, asdict
import json
import sys


dir_path_questions = "./questions"
dir_path_play = "./play"
dir_save_game = "./save"

def main():

    # start a new game
    if len(sys.argv) == 1:  

        # players enter the game by creating a .txt file in the /play/ folder
        contestants = get_contestants(dir_path_play)
           
        # setup the game and load the question set
        game = generate_game(dir_path_questions, contestants)
        
        # save the game state
        json_string = json.dumps(asdict(game))
        with open(dir_save_game + "/save_file.json", 'w') as f:
            json.dump(json.loads(json_string), f)

    else:
        # load the save file and resume game
        with open(dir_save_game + "/save_file.json", 'r') as file:
            data = json.load(file)
            game = Game(**data)
    
    # the game continues
    game = play_game(game, dir_path_questions, dir_path_play, dir_save_game)


main()