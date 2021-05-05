import pygame

from .constants import WHITE, RED, GREY, SQUARE_SIZE


class Piece():
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = None
        self.king = False
        if self.color == WHITE:
            self.direction = -1
        elif self.color == RED:
            self.direction = 1
        self.x = 0
        self.y = 0

    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        self.calc_pos()
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def select(self, row, col, board):
        if board.board[row][col] != 0:
            return True

    def move_to(self, row, col, board):
        board.board[self.row][self.col], board.board[col][row] = board.board[row][col], board.board[self.row][self.col]
    # def __repr__(self):
    # return str(self.color)
