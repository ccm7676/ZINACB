import pygame


size = width, height = 1200, 900 
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

screen.fill(black)


def vh(vh):
    return pygame.display.get_surface().get_size()[1]/100 * vh

def vw(vw):
    return pygame.display.get_surface().get_size()[0]/100 * vw


class board():
    img = pygame.image.load("boards/Default Board.png")
    size = (int(vh(70)),int(vh(70)))
    pos = (vw(50) - size[0]/2,vh(50) - size[1]/2)











def update_win():
    board.img = pygame.transform.scale(board.img, board.size)
    screen.blit(board.img,board.pos)
    pygame.display.update()


