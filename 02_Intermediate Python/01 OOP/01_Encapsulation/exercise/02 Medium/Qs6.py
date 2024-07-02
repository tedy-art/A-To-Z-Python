"""
Question 6:
Create a Game class with private attributes
__players (a list of player names)
and
__scores (a dictionary of player names and their scores).
Implement methods to add a player, remove a player, and update a player's score.
"""


class Game:
    def __init__(self):
        self.__players = []
        self.__scores = {}

    def add_player(self, player_name):
        """Add a player to the game."""
        if player_name in self.__players:
            print(f"{player_name} already exists. Please choose another name.")
        else:
            self.__players.append(player_name)
            self.__scores[player_name] = 0
            print(f"{player_name} has been added to the game.")

    def remove_player(self, player_name):
        """Remove a player from the game."""
        if player_name in self.__players:
            self.__players.remove(player_name)
            del self.__scores[player_name]
            print(f"{player_name} has been removed from the game.")
        else:
            print(f"{player_name} is not in the game. Cannot remove.")

    def update_score(self, player_name, new_score):
        """Update the score of a player."""
        if player_name in self.__players:
            self.__scores[player_name] = new_score
            print(f"Score of {player_name} updated to {new_score}.")
        else:
            print(f"{player_name} is not in the game. Cannot update score.")


# Example usage:
game = Game()
game.add_player("Player1")
game.add_player("Player2")
game.update_score("Player1", 100)
game.update_score("Player3", 50)  # Player3 does not exist
game.remove_player("Player2")
game.remove_player("Player3")  # Player3 does not exist
