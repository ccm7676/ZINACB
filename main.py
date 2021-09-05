# game handling 
import board


class Game():
	
	def __init__(self, game_board):
		self.game_board = game_board 
		self.game_brain = game_brain


b = board.Board()
g = Game(b)


g.start_game()
