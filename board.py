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

			
			
			
		pass
		
	
			
	


b = Board()

b.print_board()
