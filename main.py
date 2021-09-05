# game handling 
import board
import generator

class Game():
	
	def __init__(self, game_board, move_generator):
		self.game_board = game_board 
		self.move_generator = move_generator
		
	def start_game(self):
		self.game_board.print_board()
		inp = input("chess pos: ").strip().lower()
		
		if (self.game_board.get_piece_at_pos(inp) == "p" or self.game_board.get_piece_at_pos(inp) == "P"):
			print(self.move_generator.get_pawn_moves(inp, self.game_board))

		if (self.game_board.get_piece_at_pos(inp) == "n" or self.game_board.get_piece_at_pos(inp) == "N"):
			print(self.move_generator.get_knight_moves(inp, self.game_board))
	
		

bo = board.Board()
move_genner = generator.MoveGenerator()
game = Game(bo, move_genner)



game.start_game()
