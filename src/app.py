from connect_4 import ConnectFour
import sys
import readline
import os


def display(board):
    column_numbers = ' 1 2 3 4 5 6'
    horizontal_separator = '-------------'
    new_line = '\n'
    vertical_separator = '|'

    column_renderer = [vertical_separator + vertical_separator.join(row) + vertical_separator for row in board]
    rows = new_line.join(column_renderer)

    return column_numbers + new_line + horizontal_separator + new_line + rows + new_line + horizontal_separator


def main():
    game = ConnectFour()
    player_one = True
    while game.in_progress:
        print(display(game.board))
        try:
            player = 1 if player_one else 2
            column = input("Enter your move player %d: " % player)
            game.select_column(column, player)
        except:
            print("*** Error occurred please try again ***")


if __name__ == '__main__':
    main()
