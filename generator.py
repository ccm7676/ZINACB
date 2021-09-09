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
        y, x = row, column

        # check if given position is a pawn
        if (board_handler.board[y][x].lower() == "p"):
            print("Generating moves for " + pawn_pos + " pawn...")

            # check if its a black pawn space in front is empty
            if(board_handler.board[y][x] == "p"):
                
                #check if pos infront is empty 
                if (board_handler.board[y+1][x] == "-"):
                    possibleMoves.append((y+1, x))
                
                #check if pawn is at starting pos
                if (y == 1):
                    possibleMoves.append((y+2, x))

                #check if theres an enemy to kill
                if(y+1 >= 0 and y+1 <= 7 and x+1 >= 0 and x+1 <= 7):
                    if(board_handler.board[y+1][x+1].isupper() == True):
                        possibleMoves.append((y+1,x+1))
                
                #check if theres an enemy to kill
                if(y+1 >= 0 and y+1 <= 7 and x-1 >= 0 and x-1 <= 7):
                    if(board_handler.board[y+1][x-1].isupper() == True):
                        possibleMoves.append((y+1,x-1))

            if (board_handler.board[y][x] == "P"):

                if(y == 6):
                    possibleMoves.append((y-2, x))

                # check if its a white pawn and space in front is empty
                if (board_handler.board[y-1][x] == "-"):
                    possibleMoves.append((y-1, x))
                
                #check if theres an enemy to kill
                if(y-1 >= 0 and y-1 <= 7 and x+1 >= 0 and x+1 <= 7):
                    if(board_handler.board[y-1][x+1].lower() == True):
                        possibleMoves.append((y-1,x+1))

                #check if theres and enemy to kill

                if(y-1 >= 0 and y-1 <= 7 and x-1 >= 0 and x-1 <= 7):
                    if(board_handler.board[y-1][x-1].lower() == True):
                        possibleMoves.append((y-1,x-1))
                


        possibleMoves = ["".join(
            [board_handler.index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]

        return possibleMoves

    def get_knight_moves(self, knight_pos, board_handler):
        possibleMoves = []
        
        column, row = list(knight_pos.strip().lower())
        row = int(row) - 1
        column = board_handler.alpha_to_index[column]
        y,x = row, column
        
        movePosKnight = [(y+2, x-1), (y-1, x+2), (y-2, x-1), (y+2, x+1), (y+1,x+2),(y+1,x-1), (y-2, x+1)]

        #small knight
        if (board_handler.board[y][x]  == "n"):
            for i in movePosKnight:
                if(i[0] >= 0 and i[0] <= 7 and i[1] >= 0 and i[1] <= 7):
                    if(board_handler.board[i[0]][i[1]] == "-" or board_handler.board[i[0]][i[1]].isupper() == True):
                        possibleMoves.append(i)
        
        #big knight
        if (board_handler.board[y][x] == "N"):
            for i in movePosKnight:
                if(i[0] >= 0 and i[0] <= 7 and i[1] >= 0 and i[1] <= 7):
                    if(board_handler.board[i[0]][i[1]] == "-" or board_handler.board[i[0]][i[1]].islower() == True):
                        possibleMoves.append(i)

                
        possibleMoves =["".join([board_handler.index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]

        return possibleMoves


    def get_king_moves(self, king_pos, board_handler):
        possibleMoves = []
        
        column, row = list(king_pos.strip().lower())
        row = int(row) - 1
        column = board_handler.alpha_to_index[column]
        y,x = row, column

        movePosKing = [(y+1,x), (y+1,x+1), (y,x+1),(y-1,x+1),(y-1,x),(y-1,x-1),(y,x-1),(y+1,x-1)]

        if (board_handler.board[y][x]  == "k"):
            for i in movePosKing:
                if(i[0] >= 0 and i[0] <= 7 and i[1] >= 0 and i[1] <= 7):
                    if(board_handler.board[i[0]][i[1]] == "-" or board_handler.board[i[0]][i[1]].isupper() == True):
                        possibleMoves.append(i)
        
        if (board_handler.board[y][x] == "K"):
            for i in movePosKing:
                if(i[0] >= 0 and i[0] <= 7 and i[1] >= 0 and i[1] <= 7):
                    if(board_handler.board[i[0]][i[1]] == "-" or board_handler.board[i[0]][i[1]].islower() == True):
                        possibleMoves.append(i)
        
        possibleMoves =["".join([board_handler.index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]

        return possibleMoves
    
    def get_rook_moves(self, rook_pos, board_handler):
        possibleMoves = []
        
        column, row = list(rook_pos.strip().lower())
        row = int(row) - 1
        column = board_handler.alpha_to_index[column]
        y,x = row, column

        if(board_handler.board[y][x] == "r"):
            
            for i in range(8):
                if(y-i >= 0 and y-i <= 7):
                    if(board_handler.board[y-i][x] == "-"):
                        possibleMoves.append((x,y-i))
                    elif(board_handler.board[y-i][x].isupper() == True):
                        possibleMoves.append((x, y-i))
                        break
                    else:
                        break

            for i in range(8):
                if(y+i >= 0 and y+i <= 7):
                    if(board_handler.board[y+i][x] == "-"):
                        possibleMoves.append((x,y+i))
                    elif(board_handler.board[y+i][x].isupper() == True):
                        possibleMoves.append((x, y+i))
                        break
                    else:
                        break

            for i in range(8):
                if(x-i >= 0 and x-i <= 7):
                    if(board_handler.board[y][x-i] == "-"):
                        possibleMoves.append((x-i,y))
                    elif(board_handler.board[y][x-i].isupper() == True):
                        possibleMoves.append((x-i, y))
                        break
                    else:
                        break

            for i in range(8):
                if(x+i >= 0 and x+i <= 7):
                    if(board_handler.board[y][x+i] == "-"):
                        possibleMoves.append((x+i,y))
                    elif(board_handler.board[y][x+i].isupper() == True):
                        possibleMoves.append((x+i, y))
                        break
                    else:
                        break
        if(board_handler.board[y][x] == "R"):
            
            for i in range(8):
                if(y-i >= 0 and y-i <= 7):
                    if(board_handler.board[y-i][x] == "-"):
                        possibleMoves.append((x,y-i))
                    elif(board_handler.board[y-i][x].islower() == True):
                        possibleMoves.append((x, y-i))
                        break
                    else:
                        break

            for i in range(8):
                if(y+i >= 0 and y+i <= 7):
                    if(board_handler.board[y+i][x] == "-"):
                        possibleMoves.append((x,y+i))
                    elif(board_handler.board[y+i][x].islower() == True):
                        possibleMoves.append((x, y+i))
                        break
                    else:
                        break

            for i in range(8):
                if(x-i >= 0 and x-i <= 7):
                    if(board_handler.board[y][x-i] == "-"):
                        possibleMoves.append((x-i,y))
                    elif(board_handler.board[y][x-i].islower() == True):
                        possibleMoves.append((x-i, y))
                        break
                    else:
                        break

            for i in range(8):
                if(x+i >= 0 and x+i <= 7):
                    if(board_handler.board[y][x+i] == "-"):
                        possibleMoves.append((x+i,y))
                    elif(board_handler.board[y][x+i].islower() == True):
                        possibleMoves.append((x+i, y))
                        break
                    else:
                        break

        possibleMoves =["".join([board_handler.index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]

        return possibleMoves
                    


                
            
            