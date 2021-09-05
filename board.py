class Board():
	# pieces matrix; to be linked with other pieces classes 
	
	board = [["r", "n", "b", "q", "k", "b", "n", "r"], # black pieces
			["p", "p", "p", "p", "p", "p", "p", "p"], # black pawns
			["nul", "nul", "nul", "nul", "nul", "nul", "nul", "nul"], # empty
			["nul", "nul", "nul", "nul", "nul", "nul", "nul", "nul"], # empty
			["nul", "nul", "nul", "nul", "nul", "nul", "nul", "nul"], # empty
			["nul", "nul", "nul", "nul", "nul", "nul", "nul", "nul"], # empty
			["P", "P", "P", "P", "P", "P", "P", "P"], # white pawns
			["R", "N", "B", "Q", "K", "B", "N", "R"]] # white pieces
			
	# print out the matrix neatly in the console
		
	def print_board(self):
		for i in range(len(self.board)):
			for j in self.board[i]:
				print(j,end=" ")
			print("\n")

	#the possible moves function returns possible moves for the piece on the selected possition
	def possible_moves(self, x,y):
		possibleMoves = []
		
		#checks if selected possition is a small pawn
		if(self.board[y][x] == "p"):

			#checks if pawn can move forward
			if(self.board[y-1][x] == "nul"):
				possibleMoves.append((x,y-1))
				
			
			#checks if pawn can kill
			if(self.board[y-1][x+1].isupper() == False):
				possibleMoves.append((x+1,y-1))

			#checks if pawn can kill
			if(self.board[y-1][x-1].isupper() == False):
				possibleMoves.append((x-1,y+1))
			
		#checks if selected possition is a big pawn
		if(self.board[y][x] == "P"):

			#checks if pawn can move forward
			if(self.board[y+1][x] == "nul"):
				possibleMoves.append((x,y+1))
				
			
			#checks if pawn can kill
			if(self.board[y+1][x+1].islower() == True):
				possibleMoves.append((x+1,y+1))

			#checks if pawn can kill
			if(self.board[y+1][x-1].islower() == True):
				possibleMoves.append((x-1,y+1))
			
		#checks if selected position is a small king
		elif(self.board[y][x] == "k"):
			
			#list of positions around king so the for loop can loop through it and reduce the amount of if statements 
			movePosKing = [(x,y+1), (x+1,y+1), (x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1)]

			#loops around the posAroundKings array
			for i in movePosKing:
				if(self.board[i[1]][i[0]] == "nul" or self.board[i[1]][i[0]].isupper() == True):
					if(i[1] >= 0  and i[0] >= 0):
						possibleMoves.append(i)
		
		#checks if selected position is big King
		elif(self.board[y][x] == "K"):
			
			#list of positions around king so the for loop can loop through it and reduce the amount of if statements 
			movePosKing = [(x,y+1), (x+1,y+1), (x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1)]

			#loops around the posAroundKings array
			for i in movePosKing:
				if(self.board[i[1]][i[0]] == "nul" or self.board[i[1]][i[0]].islower() == True):
					if(i[1] >= 0  and i[0] >= 0):
						possibleMoves.append(i)
					
		#checks if selected position is small knight
		elif(self.board[y][x] == "n"):
			movePosKnight = [(x-1,y-2),(x+1,y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2), (x-2,y+1),(x-2,y-1)]
			
			for i in movePosKnight:
				if(self.board[i[1]][i[0]] == "nul" or self.board[i[1]][i[0]].isupper() == True):
					if(i[1] >= 0  and i[0] >= 0):
						possibleMoves.append(i)

		#checks if selected position is small knight
		elif(self.board[y][x] == "N"):
			movePosKnight = [(x-1,y-2),(x+1,y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2), (x-2,y+1),(x-2,y-1)]
			
			for i in movePosKnight:
				if(self.board[i[1]][i[0]] == "nul" or self.board[i[1]][i[0]].islower() == True):
					if(i[1] >= 0  and i[0] >= 0):
						possibleMoves.append(i)


		elif(self.board[y][x].lower() == "q"):
			print("queen")

		elif(self.board[y][x].lower() == "b"):
			print("bishop")

		elif(self.board[y][x].lower() == "r"):
			print("rook")
		
		return possibleMoves
	


b = Board()

b.print_board()

while True:
	inp = input("x, y:").split(",")
	print(b.possible_moves(int(inp[0]),int(inp[1])))