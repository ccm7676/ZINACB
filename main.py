# game handling 
import brain
import board


class Game():
	
	def __init__(self, game_board, game_brain):
		self.game_board = game_board 
		self.game_brain = game_brain
		
	def start_game(self):
		self.game_board.print_board()
		inp = input("pos (chess notation): ")
			
		
		print(self.game_brain.gen_possible_moves(inp, self.game_board))
		self.game_board.print_board()


b = board.Board()
br = brain.Zinca("standard")
g = Game(b, br)


g.start_game()
