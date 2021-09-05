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
		y,x = row, column
		
		print("i: " + str(y))
		print("j: " + str(x))
		

		if(board.board[y][x] == "P"):

			#checks if pawn can move forward
			if(board.board[y-1][x] == "nul"):
				possibleMoves.append((x,y-1))
				
			
			#checks if pawn can kill
			if(board.board[y-1][x+1].islower() == True):
				possibleMoves.append((x+1,y-1))

			#checks if pawn can kill
			if(board.board[y-1][x-1].islower() == True):
				possibleMoves.append((x-1,y+1))
			
		#checks if selected possition is a big pawn
		if(board.board[y][x] == "p"):

			#checks if pawn can move forward
			if(board.board[y+1][x] == "nul"):
				possibleMoves.append((x,y+1))
				
			
			#checks if pawn can kill
			if(board.board[y+1][x+1].isupper() == True):
				possibleMoves.append((x+1,y+1))

			#checks if pawn can kill
			if(board.board[y+1][x-1].isupper() == True):
				possibleMoves.append((x-1,y+1))
			
		#checks if selected position is a small king
		elif(board.board[y][x] == "k"):
			
			#list of positions around king so the for loop can loop through it and reduce the amount of if statements 
			movePosKing = [(x,y+1), (x+1,y+1), (x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1)]

			#loops around the posAroundKings array
			for i in movePosKing:
				if(board.board[i[1]][i[0]] == "nul" or board.board[i[1]][i[0]].isupper() == True):
					possibleMoves.append(i)
		
		#checks if selected position is big King
		elif(board.board[y][x] == "K"):
			
			#list of positions around king so the for loop can loop through it and reduce the amount of if statements 
			movePosKing = [(x,y+1), (x+1,y+1), (x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1)]

			#loops around the posAroundKings array
			for i in movePosKing:
				if(board.board[i[1]][i[0]] == "nul" or board.board[i[1]][i[0]].islower() == True):
					possibleMoves.append(i)
					
		#checks if selected position is small knight
		elif(board.board[y][x] == "n"):
			movePosKnight = [(x-1,y-2),(x+1,y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2), (x-2,y+1),(x-2,y-1)]
			
			for i in movePosKnight:
				if(board.board[i[1]][i[0]] == "nul" or board.board[i[1]][i[0]].isupper() == True):
					possibleMoves.append(i)

		#checks if selected position is small knight
		elif(board.board[y][x] == "N"):
			movePosKnight = [(x-1,y-2),(x+1,y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2), (x-2,y+1),(x-2,y-1)]
			
			for i in movePosKnight:
				if(board.board[i[1]][i[0]] == "nul" or board.board[i[1]][i[0]].islower() == True):
					possibleMoves.append(i)

		#the rook, queen, and bishop will have their own selecting mechanisms because they can go infinitely in several directions
		elif(board.board[y][x].lower() == "q"):
			print("queen")

		elif(board.board[y][x].lower() == "b"):
			print("bishop")

		elif(board.board[y][x] == "r"):
			#I WANNA DIE
			#ROOK CAN SUCK MY COOK
			#check how many possible moves in one direction
			for i in range(10):
				if(y-i >= 0 and y-i <= 7):
					if(board.board[y-i][x] == "nul"):
						possibleMoves.append((x,y-i))
					else:
						if(board.board[y-i][x].isupper() == True):
							possibleMoves.append((x,y-i))
							i = 11
						else:
							i = 11
				else:
					i = 11
			#check how many possible moves in one direction
			for i in range(10):
				if(y+i >= 0 and y+i <= 7):
					if(board.board[y+i][x] == "nul"):
						possibleMoves.append((x,y+i))
					else:
						if(board.board[y+i][x].isupper() == True):
							possibleMoves.append((x,y+i))
							i = 11
						else:
							i = 11
				else:
					i = 11
			#check how many possible moves in one direction
			for i in range(10):
				if(x+i >= 0 and x+i <= 7):
					if(board.board[y][x+i] == "nul"):
						possibleMoves.append((x+i,y))
					else:
						if(board.board[y][x+i].isupper() == True):
							possibleMoves.append((x+i,y))
							i = 11
						else:
							i = 11
				else:
					i=11
			#check how many possible moves in one direction
			for i in range(10):
				if(x-1 >= 0 and x-1 <= 7):
					if(board.board[y][x-i] == "nul"):
						possibleMoves.append((x-i,y))
					else:
						if(board.board[y][x-i].isupper() == True):
							possibleMoves.append((x-i,y))
							i = 11
						else:
							i = 11
				else:
					i = 11
		
		return possibleMoves
