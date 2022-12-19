import random
import time

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
        self.players = [Player('Player 1 (PC)', self.colors[0]), Player('Player 2 (user)', self.colors[1])]
        self.players_number = len(self.players)
        self.index_current_player = self.set_first_player()
        # self.index_current_player = 0
        self.winner = None

        self.max_score = self.size ** 2
        self.min_score = -self.max_score
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
        """Перевірка, чи може гравець походити у цю клітинку (cell - список або множина у вигляді [i, j] або (i, j))"""
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
    '''------------------------------------------------------'''
    def is_move(self, field, index_player, cell):
        """Перевірка, чи може гравець походити у цю клітинку (cell - список або множина у вигляді [i, j] або (i, j))"""
        color_op = 'blue' if self.players[index_player].color == 'red' else 'red'
        if cell[0] - 1 != -1:
            if field[cell[0] - 1][cell[1]] == color_op:
                return False
        if cell[0] + 1 != self.size:
            if field[cell[0] + 1][cell[1]] == color_op:
                return False
        if cell[1] - 1 != -1:
            if field[cell[0]][cell[1] - 1] == color_op:
                return False
        if cell[1] + 1 != self.size:
            if field[cell[0]][cell[1] + 1] == color_op:
                return False
        return True

    def is_looser(self, field, index_player):
        """Перевірка, чи програв гравець"""
        index_opp = (index_player + 1) % self.players_number
        for i in range(self.size):
            for j in range(self.size):
                if not field[i][j] == '-':
                    if field[i][j] == '0':
                        if self.is_move(field, index_player, [i, j]):
                            return False
        return True

    def minimax(self, field, depth, index_player):
        """Мінімакс"""
        result = self.is_looser(field, index_player)

        if result:
            if not index_player:
                return self.min_score + depth
            else:
                return self.max_score - depth

        if not index_player:
            best_score = -float('inf')

            for i in range(self.size):
                for j in range(self.size):
                    if field[i][j] == '0':
                        if self.is_turn(index_player, [i, j]):
                            field[i][j] = self.players[index_player].color
                            index_next_player = (index_player + 1) % 2
                            best_score = max(best_score, self.minimax(field, depth + 1, index_next_player))
                            field[i][j] = '0'

            return best_score
        else:
            best_score = float('inf')

            for i in range(self.size):
                for j in range(self.size):
                    if field[i][j] == '0':
                        if self.is_turn(index_player, [i, j]):
                            field[i][j] = self.players[index_player].color
                            index_next_player = (index_player + 1) % 2
                            best_score = min(best_score, self.minimax(field, depth + 1, index_next_player))
                            field[i][j] = '0'

            return best_score
        return

    def find_best_move(self, field, index_player):
        """Знаходження найкращого ходу"""
        best_score = float('inf') if index_player else -float('inf')
        best_move = None
        for i in range(self.size):
            for j in range(self.size):
                if field[i][j] == '0':
                    if self.is_move(field, index_player, [i, j]):
                        field[i][j] = self.players[index_player].color
                        index_next_player = (index_player + 1) % 2
                        # move_score = self.minimax(field, 0, index_next_player)
                        move_score = self.alpha_beta_prunning(field, 0, index_next_player, -float('inf'), float('inf'))
                        field[i][j] = '0'

                        if not index_player:
                            if move_score > best_score:
                                best_score = move_score
                                best_move = [i, j]
                        else:
                            if move_score < best_score:
                                best_score = move_score
                                best_move = [i, j]

        return best_score, best_move

    def alpha_beta_prunning(self, field, depth, index_player, alpha, beta):
        """Альфа-бета відсікання"""
        result = self.is_looser(field, index_player)

        if result:
            if not index_player:
                return self.min_score + depth
            else:
                return self.max_score - depth

        if not index_player:
            best_score = -float('inf')
            is_break = False
            for i in range(self.size):
                for j in range(self.size):
                    if field[i][j] == '0':
                        if self.is_turn(index_player, [i, j]):
                            field[i][j] = self.players[index_player].color
                            index_next_player = (index_player + 1) % 2
                            best_score = max(best_score, self.alpha_beta_prunning(field, depth + 1, index_next_player, alpha, beta))
                            field[i][j] = '0'
                            alpha = max(alpha, best_score)
                            if beta <= alpha:
                                is_break = True
                                break
                if is_break:
                    break

            return best_score
        else:
            best_score = float('inf')
            is_break = False
            for i in range(self.size):
                for j in range(self.size):
                    if field[i][j] == '0':
                        if self.is_turn(index_player, [i, j]):
                            field[i][j] = self.players[index_player].color
                            index_next_player = (index_player + 1) % 2
                            best_score = min(best_score, self.alpha_beta_prunning(field, depth + 1, index_next_player, alpha, beta))
                            field[i][j] = '0'
                            beta = min(beta, best_score)
                            if beta <= alpha:
                                is_break = True
                                break
                if is_break:
                    break

            return best_score
        return

def main():
    """Початок гри"""
    GAME_FIELD = [['-', '0', '0', '-'],
                  ['0', '0', '0', '0'],
                  ['0', '0', '0', '0'],
                  ['-', '0', '0', '-']]
    # game = Game(GAME_FIELD2, COLORS)
    #
    # while True:
    #     print('-'*100)
    #     print('\033[36m', game.players[game.index_current_player].name, ' : ' , game.players[game.index_current_player].color, '\033[00m', sep='')
    #     game.output()
    #     numb = int(input('\033[93mInput the cell\'s number: \033[00m'))
    #     i, j = numb // game.size, numb % game.size
    #     if not (0 <= numb < game.size ** 2) or game.game_field[i][j] != '0' or not game.is_turn(game.index_current_player, [i, j]):
    #         print('\033[91mThe number is wrong\033[00m')
    #         continue
    #     else:
    #         game.set_cell([i, j], game.players[game.index_current_player].color)
    #         if game.is_winner(game.index_current_player):
    #             game.output()
    #             print('\033[47m\033[90m', 'The winnner is: ', game.winner.name, ' (color: ', game.winner.color, ')', '\033[00m', sep='')
    #             break
    #         game.set_next_player()

    # --------------------------------------------------------------------
    game = Game(GAME_FIELD, COLORS)

    while True:
        print('-' * 100)
        print('\033[36m', game.players[game.index_current_player].name, ' : ',
              game.players[game.index_current_player].color, '\033[00m', sep='')
        game.output()
        if game.index_current_player:
            numb = int(input('\033[93mInput the cell\'s number: \033[00m'))
            i, j = numb // game.size, numb % game.size
            if not (0 <= numb < game.size ** 2) or game.game_field[i][j] != '0' or not game.is_turn(game.index_current_player, [i, j]):
                print('\033[91mThe number is wrong\033[00m')
                continue
            else:
                game.set_cell([i, j], game.players[game.index_current_player].color)
                if game.is_winner(game.index_current_player):
                    game.output()
                    print('\033[47m\033[90m', 'The winnner is: ', game.winner.name, ' (color: ', game.winner.color, ')',
                          '\033[00m', sep='')
                    break
                game.set_next_player()
        else:
            time_start = time.time_ns()
            best_score, best_move = game.find_best_move(game.game_field, game.index_current_player)
            time_end = time.time_ns()
            print('Best score for PC: ', best_score, '  Time in miliseconds:', (time_end-time_start) / 1000/ 1000)
            game.set_cell([best_move[0], best_move[1]], game.players[game.index_current_player].color)
            if game.is_winner(game.index_current_player):
                game.winner = game.players[game.index_current_player]
                game.output()
                print('\033[47m\033[90m', 'The winnner is: ', game.winner.name, ' (color: ', game.winner.color, ')',
                      '\033[00m', sep='')
                break
            game.set_next_player()

    return

if __name__ == "__main__":
    main()