from ast import Pass
from lib2to3.pygram import python_grammar_no_print_statement
import pygame
from checkers.constants import RED, WHITE, WIDTH, HEIGHT, SQUARE_SIZE
from checkers.piece import Piece
from checkers.game import Game
from DFS.algorithm import dfs

FPS = 60

WIN =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = dfs(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)


        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False

           if event.type == pygame.MOUSEBUTTONDOWN:
                Pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(Pos)
                game.select(row, col)

        game.update()   
    
    pygame.quit()

main()