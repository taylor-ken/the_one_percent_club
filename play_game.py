from classes import Question
from dataclasses import dataclass, asdict
import time
import json

def play_game(game, dir_path_questions, dir_path_play, dir_save_game):

    with open(dir_path_questions + "/_current_question.txt", "w") as file:
                    file.write("Get ready to play!")
    while game.playing_count > 1:
        question_link = game.questions[game.current_round]
        print(question_link)
        with open(question_link, 'r') as file:
                current_question = Question(**json.load(file))
                input("Press Enter to post question...\n")
                with open(dir_path_questions + "/_current_question.txt", "w") as file:
                    file.write(current_question.question + "\n\n")
                    if current_question.is_multiple_choice:
                        if len(current_question.option_A) > 0:
                            file.write("(A) " + current_question.option_A + "\n")
                        if len(current_question.option_B) > 0:    
                            file.write("(B) " + current_question.option_B + "\n")
                        if len(current_question.option_C) > 0:
                            file.write("(C) " + current_question.option_C + "\n")
                        if len(current_question.option_D) > 0:
                            file.write("(D) " + current_question.option_D + "\n")
        
        # give the players time to answer
        time.sleep(30)
        #print(game.contestants_in)
        wrong_answers = []
        for i in range(len(game.contestants)):
            with open(dir_path_play + "/" + game.contestants[i].name, 'r') as file:
                game.contestants[i].answer = str(file.read()).strip()
                if game.contestants[i].answer.upper() == 'PASS':
                    if game.contestants[i].has_pass == False:
                        if game.contestants[i].is_eliminated == False:
                            game.playing_count -= 1
                        game.contestants[i].is_eliminated = True
                    else:
                        game.contestants[i].has_pass = False
                elif game.contestants[i].answer.upper() != current_question.answer.upper():
                    if game.contestants[i].is_eliminated == False:
                        game.playing_count -= 1
                    game.contestants[i].is_eliminated = True
                    
            name = game.contestants[i].name.split('.')
            print(name[0], game.contestants[i].answer)

            # at the end of round 5 everyone gets a free pass for a question they don't know
            if game.current_round == 4:
                game.contestants[i].has_pass = True
        game.current_round += 1

        print("Correct answer was: ", current_question.answer)
        print("\nRemaining contestants:")
        for i in range(len(game.contestants)):
            if game.contestants[i].is_eliminated == False:
                name = game.contestants[i].name.split('.')
                print(name[0])

        # save the game state
        json_string = json.dumps(asdict(game))
        with open(dir_save_game + "/save_file.json", 'w') as f:
            json.dump(json.loads(json_string), f)
    print(game.playing_count)
    if game.playing_count < 1:
        print("Everyone sucks. Game over.")
    return game