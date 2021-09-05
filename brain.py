# the brain of the engine, where rules are defined

class Zinca():
	
	# init game var for now is just for standard chess, but if we wanna implement antichess or chess960 we're gonna have to take this var into account

	def __init__(self, game_type):
		self.game_type = game_type
		
	# move generator, pass board param
	# the possible moves function returns possible moves for the piece on the selected possition
	
	def gen_possible_moves(self, pos, board): # takes in chess coords
		possibleMoves = []
		
		column, row = list(pos.strip().lower())
		row = int(row) - 1
		column = board.alpha_to_index[column]
		i,j = row, column
		
		print("i: " + str(i))
		print("j: " + str(j))
		
		
		# check if pos is a rook
		
		# check if pos is a knight
		
		# etc
			
		
		return possibleMoves
