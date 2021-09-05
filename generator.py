"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || | ____    ____ | || |     ____     | || |  _______     | || |  _________   | |
| |   /  ___  |  | || ||_   \  /   _|| || |   .'    `.   | || | |_   __ \    | || | |  _   _  |  | |
| |  |  (__ \_|  | || |  |   \/   |  | || |  /  .--.  \  | || |   | |__) |   | || | |_/ | | \_|  | |
| |   '.___`-.   | || |  | |\  /| |  | || |  | |    | |  | || |   |  __ /    | || |     | |      | |
| |  |`\____) |  | || | _| |_\/_| |_ | || |  \  `--'  /  | || |  _| |  \ \_  | || |    _| |_     | |
| |  |_______.'  | || ||_____||_____|| || |   `.____.'   | || | |____| |___| | || |   |_____|    | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""







class MoveGenerator():
	
	""" the move generator class. the engine learns 
		to play chess here and generates every possible move for 
		pieces
	"""
	
	# the pawn pos param is passed to the function to specify which pawn Zinca has to look at
	# the var board handler is a reference to the Board object which is created in main.py
	def get_pawn_moves(self, pawn_pos, board_handler):
		
		possibleMoves = []
		
		column, row = list(pawn_pos.strip().lower())
		row = int(row) - 1
		column = board_handler.alpha_to_index[column]
		y,x = row, column
		
		# check if given position is a pawn
		if (board_handler.board[y][x] == "P" or board_handler.board[y][x] == "p"):
			print("Generating moves for " + pawn_pos + " pawn...")
			
			# check if its a black pawn space in front is empty
			if (board_handler.board[y][x] == "p" and  board_handler.board[y+1][x] == "-"):
				possibleMoves.append((y+1,x))
			
			if (board_handler.board[y][x] == "p" and pawn_pos == "a2" or pawn_pos == "b2" or pawn_pos == "c2"
				or pawn_pos == "d2" or pawn_pos == "e2" or pawn_pos == "f2" or pawn_pos == "g2" or pawn_pos == "h2"):

				possibleMoves.append((y+2, x))
			
			
			if (board_handler.board[y][x] == "P" and pawn_pos == "a7" or pawn_pos == "b7" or pawn_pos == "c7"
				or pawn_pos == "d7" or pawn_pos == "e7" or pawn_pos == "f7" or pawn_pos == "g7" or pawn_pos == "h7"):

				possibleMoves.append((y-2,x))
				
			# check if its a white pawn and space in front is empty
			if (board_handler.board[y][x] == "P" and board_handler.board[y-1][x] == "-"):
				possibleMoves.append((y-1,x))
			



		
		possibleMoves =["".join([board_handler.index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]
		
		return possibleMoves
		
	
	def get_knight_moves(self, knight_pos, board_handler):
		possibleMoves = []
		
		column, row = list(knight_pos.strip().lower())
		row = int(row) - 1
		column = board_handler.alpha_to_index[column]
		y,x = row, column
	

		if(board_handler.board[y][x] == "n"):
			movePosKnight = [(x-1,y-2),(x+1,y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2), (x-2,y+1),(x-2,y-1)]
			
			for i in movePosKnight:
				if(i[1] >= 0  and i[0] >= 0 and i[0] <= 7 and i[1] <= 7):
					if(board_handler.board[i[1]][i[0]] == "-" or board_handler.board[i[1]][i[0]].isupper() == True):
				
							possibleMoves.append(i)

				#checks if selected position is small knight
		elif (board_handler.board[y][x] == "N"):
			movePosKnight = [(x-1,y-2),(x+1,y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2), (x-2,y+1),(x-2,y-1)]
				
			for i in movePosKnight:
				if(i[1] >= 0  and i[0] >= 0 and i[0] <= 7 and i[1] <= 7):
					if(board_handler.board[i[1]][i[0]] == "-" or board_handler.board[i[1]][i[0]].islower() == True):
						
						possibleMoves.append(i)

		possibleMoves =["".join([board_handler.index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]
		
		
		return possibleMoves


	
		