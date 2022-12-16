import random

GAME_FIELD1 = [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
               [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
GAME_FIELD2 = [['-', '0', '0', '-'],
               ['0', '0', '0', '0'],
               ['0', '0', '0', '0'],
               ['-', '0', '0', '-']]
COLORS = ['red', 'blue']

class Player():
    """Гравець"""
    def __init__(self, name, color):
        """Конструктор"""
        self.name = name
        self.color = color
        return

class Game():
    """Гра"""
    def __init__(self, GAME_FIELD, COLORS):
        """Конструктор"""
        self.size = len(GAME_FIELD)
        self.game_field = GAME_FIELD
        self.colors = COLORS
        self.players = [Player('Player 1', self.colors[0]), Player('Player 2', self.colors[1])]
        self.players_number = len(self.players)
        self.index_current_player = self.set_first_player()
        self.winner = None
        return

    def set_first_player(self):
        """Визначення першого гравця"""
        return random.randint(0, self.players_number - 1)

    def set_next_player(self):
        """Визначення наступного гравця"""
        self.index_current_player = (self.index_current_player + 1) % self.players_number
        return self.index_current_player

    def set_cell(self, cell, color):
        """Зафарбувати комірку у заданий колір"""
        if self.game_field[cell[0]][cell[1]] == '0':
            self.game_field[cell[0]][cell[1]] = color
        return

    def is_winner(self, index_player):
        """Перевірка, чи виграв гравець"""
        index_opp = (index_player + 1) % self.players_number
        for i in range(self.size):
            for j in range(self.size):
                if not self.game_field[i][j] == '-':
                    if self.game_field[i][j] == '0':
                        if self.is_turn(index_opp, [i, j]):
                            return False
        self.winner = self.players[index_player]
        return True

    def is_turn(self, index_player, cell):
        """Перевірка, чи може гравець походити у цю клітинку (cell - список або множина у вигляді [i, j] або (i, j)"""
        color_op = 'blue' if self.players[index_player].color == 'red' else 'red'
        if cell[0] - 1 != -1:
            if self.game_field[cell[0] - 1][cell[1]] == color_op:
                return False
        if cell[0] + 1 != self.size:
            if self.game_field[cell[0] + 1][cell[1]] == color_op:
                return False
        if cell[1] - 1 != -1:
            if self.game_field[cell[0]][cell[1] - 1] == color_op:
                return False
        if cell[1] + 1 != self.size:
            if self.game_field[cell[0]][cell[1] + 1] == color_op:
                return False
        return True

    def output(self):
        """Вивід поля"""
        print('\nThe game\'s field:')
        for i in self.game_field:
            for j in i:
                color = None
                if j[0] == '-':
                    color = '\033[40m'
                elif j[0] == '0':
                    color = '\033[47m'
                elif j[0] == 'r':
                    color = '\033[41m'
                else:
                    color = '\033[44m'
                print(color, j[0], '\033[00m', sep='', end='')
            print()
        return

def main():
    """Початок гри"""
    game = Game(GAME_FIELD2, COLORS)

    while True:
        print('-'*100)
        print('\033[36m', game.players[game.index_current_player].name, ' : ' , game.players[game.index_current_player].color, '\033[00m', sep='')
        game.output()
        numb = int(input('\033[93mInput the cell\'s number: \033[00m'))
        i, j = numb // game.size, numb % game.size
        if not (0 <= numb < game.size ** 2) or game.game_field[i][j] != '0' or not game.is_turn(game.index_current_player, [i, j]):
            print('\033[91mThe number is wrong\033[00m')
            continue
        else:
            game.set_cell([i, j], game.players[game.index_current_player].color)
            if game.is_winner(game.index_current_player):
                game.output()
                print('\033[47m\033[90m', 'The winnner is: ', game.winner.name, ' (color: ', game.winner.color, ')', '\033[00m', sep='')
                break
            game.set_next_player()
    return

if __name__ == "__main__":
    main()