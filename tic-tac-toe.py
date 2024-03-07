"""
Tick-tack-toe game in the console
"""

import os


class Cell:
    def __init__(self, num):
        self.num = num
        self.symbol = ' '

    def __str__(self):
        return self.symbol


class Board:

    def __init__(self):

        self.cells = [Cell(i + 1) for i in range(9)]

    def display(self):

        for i in range(3):

            print('-------------')
            out = '| '
            for j in range(3):

                out += str(self.cells[i * 3 + j]) + ' | '
            print(out)

        print('-------------')

    def update(self, cell_num, symbol):

        if self.cells[cell_num - 1].symbol == ' ':
            self.cells[cell_num - 1].symbol = symbol

            return True

        else:
            return False

    def is_full(self):

        return all(cell.symbol != ' ' for cell in self.cells)

    def is_game_over(self):

        for i in range(3):

            if (self.cells[i * 3].symbol == self.cells[i * 3 + 1].symbol == self.cells[i * 3 + 2].symbol
                    and self.cells[i * 3].symbol != ' '):

                return True

        for i in range(3):

            if (self.cells[i].symbol == self.cells[i + 3].symbol == self.cells[i + 6].symbol
                    and self.cells[i].symbol != ' '):

                return True

        if self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol and self.cells[0].symbol != ' ':

            return True

        if self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol and self.cells[2].symbol != ' ':

            return True

        return False


class Player:

    def __init__(self, name, symbol):

        self.name = name
        self.symbol = symbol
        self.score = 0

    def get_move(self):

        try:

            cell_num = int(input(self.name + ', enter cell number: '))
            return cell_num

        except ValueError:

            print('Please enter a number.')
            return self.get_move()


class Game:

    def __init__(self, player_1, player_2):

        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()
        self.current_player = player_1

    def play_turn(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.current_player.name + '\'s turn:\n')
        self.board.display()
        cell_num = self.current_player.get_move()

        while not self.board.update(cell_num, self.current_player.symbol):

            print('Cell is already occupied. Try again.')
            cell_num = self.current_player.get_move()

        if self.board.is_game_over():

            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.current_player.name + ' wins!\n')
            self.current_player.score += 1
            self.board.display()
            return True

        if self.board.is_full():

            os.system('cls' if os.name == 'nt' else 'clear')
            print('It\'s a draw!\n')
            self.board.display()
            return True

        if self.current_player == self.player_1:

            self.current_player = self.player_2

        else:
            self.current_player = self.player_1

        return False

    def play_game(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print('New game started!')
        self.board = Board()
        self.current_player = self.player_1

        while not self.board.is_game_over() and not self.board.is_full():

            if self.play_turn():

                break

        print('Score:')
        print(self.player_1.name + ': ' + str(self.player_1.score))
        print(self.player_2.name + ': ' + str(self.player_2.score))


while True:

    name1 = input('Enter name for Player 1 (X): ')
    name2 = input('Enter name for Player 2 (O): ')
    player1 = Player(name1, 'X')
    player2 = Player(name2, 'O')
    game = Game(player1, player2)
    game.play_game()

    again = input('Do you want to play again? (Y/N): ')

    if again.lower() != 'y':
        break

print('Thanks for playing!')
