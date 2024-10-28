import numpy as np


def roll_dice():
    return np.random.randint(1, 7)


def players_play(number_of_players: int) -> str:
    players_score = [0 for _ in range(number_of_players)]

    winning_score = 30
    while True:
        for i in range(number_of_players):
            while players_score[i] < winning_score:
                try:
                    print(f"Your total score {players_score[i]}")
                    player_continue = str(
                        input(f"\nRoll the dice(y\\n) player{i+1}: \n")
                    )
                    if player_continue.lower() == "y":
                        score = roll_dice()
                        print(f"You rolled {score}")
                        if score != 1:
                            players_score[i] += score
                        else:
                            players_score[i] = 0
                            break
                    else:
                        break
                except ValueError:
                    print("please input yes or no not numeric")
        if any(score >= winning_score for score in players_score):
            break

    return f"Player{players_score.index(max(players_score))+1} has won!"


while True:
    try:
        players: int = int(input("How many players will play the game(1-4): "))
        if 1 <= players <= 4:
            print(
                f"There will be {players} {'player' if players == 1 else 'players'} playing the match"
            )
            print(players_play(players))
            break
        else:
            print("Numbers out of range")
    except ValueError:
        print("Please type a number between (1-4) not alphabets")
