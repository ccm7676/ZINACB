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
		
		for i in self.board[0]:
			print(i,end=" ")
			
		print("\n")
		
		for i in self.board[1]:
			print(i, end=" ")
			
		print("\n")
			
		for i in self.board[2]:
			print(i,end=" ")
			
		print("\n")
			
		for i in self.board[3]:
			print(i,end=" ")
			
		print("\n")
			
		for i in self.board[4]:
			print(i,end=" ")
			
		print("\n")
			
		for i in self.board[5]:
			print(i,end=" ")
			
		print("\n")
			
		for i in self.board[6]:
			print(i,end=" ")
			
		print("\n")
			
		for i in self.board[7]:
			print(i,end=" ")
			
		print("\n")
			
		for i in self.board[8]:
			print(i,end=" ")
			
		print("\n")
			
			
			
		pass
		
	
			
	


b = Board()

b.print_board()
