import pygame
from checker.constants import WIDTH, HEIGHT
from checker.board import Board
WIN= pygame.display.set_mode((WIDTH,HEIGHT))
FPS=60
pygame.display.set_caption('Checkers')

def main():
    run=True
    clock=pygame.time.Clock()
    board=Board()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type ==pygame.QUIT:
                run = False
            if event.type ==pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()
main()
