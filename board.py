class Board():
	# pieces matrix; to be linked with other pieces classes 
	
	board = [["r", "n", "b", "q", "k", "b", "n", "r"], # black pieces
			["p", "p", "p", "p", "p", "p", "p", "p"], # black pawns
			["null", "null", "null", "null", "null", "null", "null", "null"], # empty
			["null", "null", "null", "null", "null", "null", "null", "null"], # empty
			["null", "null", "null", "null", "null", "null", "null", "null"], # empty
			["null", "null", "null", "null", "null", "null", "null", "null"], # empty
			["P", "P", "P", "P", "P", "P", "P", "P"], # white pawns
			["R", "N", "B", "Q", "K", "B", "N", "R"]] # white pieces
			
	# print out the matrix neatly in the console
		
	def print_board(self):
		for i in range(len(self.board)):
			for j in self.board[i]:
				print(j,end=" ")
			print("\n")

			
	def possible_moves(self, x,y):
		if(self.board[y][x].lower() == "p"):
			if(self.board[y+1][x] == "null"):
				print((x,y+1))
			if(self.board[y+1][x+1].isupper() == False):
				print((x+1,y+1))
			if(self.board[y+1][x-1].isupper() == False):
				print((x-1,y+1))

		elif(self.board[y][x].lower() == "k"):
			print("king")
		elif(self.board[y][x].lower() == "q"):
			print("queen")
		elif(self.board[y][x].lower() == "b"):
			print("bishop")
		elif(self.board[y][x].lower() == "n"):
			print("knight")
		elif(self.board[y][x].lower() == "r"):
			print("rook")
	
			
	


b = Board()

b.print_board()

while True:
	inp = input("x, y:").split(",")
	b.possible_moves(int(inp[0]),int(inp[1]))