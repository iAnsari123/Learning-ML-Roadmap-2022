# Question: Implementing the Snake and Ladder Game
class Board:
    """
    Design a Python class named [Board](cci:2:///Users/inyourdream/Downloads/OOPS Session/Assignment/OOPS Snake and Ladder Game.py:3:0-47:12) to represent the game board with snakes and ladders.

    Theory:
    The game board consists of a grid of squares, each represented by a number.
    Snakes and ladders are special squares on the board that connect two squares and can either help or hinder a player's progress.

    Operations:
    1. Add Snake: Add a snake to the board.
    2. Add Ladder: Add a ladder to the board.
    3. Check Square: Check if a square contains a snake or ladder and return the destination square if found.


    Test Cases:
    Test Case 1:
    board = Board()
    board.add_snake(14, 7)  # Snake from square 14 to square 7
    assert board.check_square(14) == 7

    Test Case 2:
    board.add_ladder(5, 19)  # Ladder from square 5 to square 19
    assert board.check_square(5) == 19

    Test Case 3:
    # Additional test cases can be added here
    pass

    """

    def __init__(self):
        # Initialize the board with an empty dictionary to store snakes and ladders
        self.board = {}

    def add_snake(self, start, end):
        # Add a snake to the board
        self.board[start] = end

    def add_ladder(self, start, end):
        # Add a ladder to the board
        self.board[start] = end

    def check_square(self, square):
        # Check if a square contains a snake or ladder and return the destination square if found
        if square in self.board:
            return self.board[square]
        else:
            return square

board = Board()
board.add_snake(14, 7)  # Snake from square 14 to square 7
assert board.check_square(14) == 7
board.add_ladder(5, 19)  # Ladder from square 5 to square 19
assert board.check_square(5) == 19

class SnakeAndLadderGame:
    """
    Design a Python class named `SnakeAndLadderGame` to represent the Snake and Ladder game.

    Theory:
    The Snake and Ladder game is a classic board game played between two or more players on a game board
    with numbered, gridded squares. The objective of the game is to reach the final square (usually labeled 100)
    first, starting from square 1.

    Rules:
    - Players take turns to roll a six-sided dice and move their token forward by the number of squares indicated by the dice roll.
    - If a player lands at the base of a ladder, they must climb the ladder to the square at the top.
    - If a player lands on the head of a snake, they must slide down to the square at the tail.
    - The first player to reach or exceed the final square wins the game.

    Operations:
    1. Roll Dice: Simulate rolling a six-sided dice and return the number rolled.
    2. Move Player: Move the current player's token forward by the number of squares indicated by the dice roll.
    3. Check for Win: Check if the current player has won the game.
    4. Display Board: Display the current position of all players on the game board.

    Test Cases:
    Test Case 1:
    game = SnakeAndLadderGame(["Player 1", "Player 2"])
    game.start_game()
    """

    def __init__(self, players):
        # Initialize the game board, players, current player, and dice
        self.board = Board()
        self.players = players
        self.current_player_index = 0
        self.dice = 6  # Six-sided dice

    def start_game(self):
        # Start the game and set the current player
        print("Game started!")
        self.display_board()

    def roll_dice(self):
        # Simulate rolling a six-sided dice and return the number rolled
        import random

        return random.randint(1, self.dice)

    def move_player(self, squares):
        # Move the current player's token forward by the number of squares indicated by the dice roll
        current_player = self.players[self.current_player_index]
        current_position = self.get_player_position(current_player)
        new_position = current_position + squares
        if new_position > 100:
            print(f"{current_player} cannot move beyond square 100.")
            return
        self.set_player_position(current_player, new_position)
        print(f"{current_player} moved to square {new_position}")

    def check_for_win(self):
        # Check if the current player has won the game
        current_player = self.players[self.current_player_index]
        current_position = self.get_player_position(current_player)
        if current_position >= 100:
            print(f"{current_player} wins!")
            return True
        return False

    def display_board(self):
        # Display the current position of all players on the game board
        print("Current board state:")
        for player in self.players:
            position = self.get_player_position(player)
            print(f"{player}: square {position}")

    def get_player_position(self, player):
        # Get the current position of a player on the board
        # For simplicity, assume players start at square 1
        if player not in self.players:
            raise ValueError("Player not found")
        # In a real implementation, you would store player positions in a data structure
        return 1

    def set_player_position(self, player, position):
        # Set the current position of a player on the board
        # For simplicity, assume players start at square 1
        if player not in self.players:
            raise ValueError("Player not found")
        # In a real implementation, you would store player positions in a data structure
        pass

game = SnakeAndLadderGame(["Player 1", "Player 2"])
game.start_game()