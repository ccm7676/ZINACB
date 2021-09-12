# board class, the class which holds the logic for the pieces and the board

class Board():
	# pieces matrix;
	
	board = [["r", "n", "b", "q", "k", "b", "n", "r"], # black pieces
			["p", "p", "p", "p", "p", "p", "p", "p"], # black pawns
			["-", "-", "-", "-", "-", "-", "-", "-"], # empty
			["-", "-", "-", "-", "-", "-", "-", "-"], # empty
			["-", "-", "r", "-", "-", "-", "-", "-"], # empty
			["-", "-", "-", "-", "-", "-", "-", "-"], # empty
			["P", "P", "P", "P", "P", "P", "P", "P"], # white pawns
			["R", "N", "B", "Q", "K", "B", "N", "R"]] # white pieces
			
	alpha_to_index = {
		"a" : 0,
		"b" : 1,
		"c" : 2,
		"d" : 3,
		"e" : 4,
		"f" : 5,
		"g" : 6,
		"h" : 7
	}
	index_to_alpha = {
		0: "a",
		1: "b",
		2: "c",
		3: "d",
		4: "e",
		5: "f",
		6: "g",
		7: "h"
	}
	
			
	# print out the matrix neatly in the console
		
	def print_board(self):
		for i in range(len(self.board)):
			for j in self.board[i]:
				print(j,end=" ")
			print("\n")
			
	def get_piece_at_pos(self, pos):
		
		column, row = list(pos.strip().lower())
		row = int(row) - 1
		column = self.alpha_to_index[column]
		y,x = row, column
		
		return self.board[y][x]





		
		
