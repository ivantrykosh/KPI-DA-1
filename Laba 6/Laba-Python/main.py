import random
import time

GAME_FIELD = [['-', '0', '0', '-'],
               ['0', '0', '0', '0'],
               ['0', '0', '0', '0'],
               ['-', '0', '0', '-']]
COLORS = ['red', 'blue']
GAME_MODES = ['easy', 'medium', 'hard']

class Player():
    """Гравець:
    name - ім'я гравця;
    color - колір гравця;
    is_max- чи є гравець max"""
    def __init__(self, name, color, is_max):
        """Створення гравця"""
        self.name = name
        self.color = color
        self.is_max = is_max
        return

    def set_is_max(self, is_max):
        """Встановлення типу гравця"""
        self.is_max = is_max
        return

class Game():
    """Гра"""
    def __init__(self, GAME_FIELD, COLORS, GAME_MODE):
        """Створення гри"""
        self.size = len(GAME_FIELD)
        self.game_field = GAME_FIELD
        self.colors = COLORS
        random.shuffle(self.colors)
        self.players = [Player('Player 1 (PC)', self.colors[0], False), Player('Player 2 (user)', self.colors[1], False)]
        self.players_number = len(self.players)
        self.index_current_player = self.set_first_player()
        self.players[self.index_current_player].set_is_max(True)
        self.winner = None
        self.max_score = self.size ** 2
        self.min_score = -self.max_score
        self.game_mode = GAME_MODE
        return

    def set_first_player(self):
        """Визначити першого гравця"""
        return random.randint(0, self.players_number - 1)

    def set_next_player(self):
        """Визначити наступного гравця"""
        self.index_current_player = (self.index_current_player + 1) % self.players_number
        return self.index_current_player

    def set_cell(self, cell, color):
        """Зафарбувати комірку у заданий колір"""
        if self.game_field[cell[0]][cell[1]] == '0':
            self.game_field[cell[0]][cell[1]] = color
        return

    def output(self):
        """Вивести ігрове поле поля"""
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

    def is_move(self, field, index_player, cell):
        """Перевірити, чи може гравець походити у цю клітинку (cell - список або множина у вигляді [i, j] або (i, j))"""
        color_opp = self.colors[0] if self.players[index_player].color == self.colors[1] else self.colors[1]
        if field[cell[0]][cell[1]] == '0':
            if cell[0] - 1 != -1:
                if field[cell[0] - 1][cell[1]] == color_opp:
                    return False
            if cell[0] + 1 != self.size:
                if field[cell[0] + 1][cell[1]] == color_opp:
                    return False
            if cell[1] - 1 != -1:
                if field[cell[0]][cell[1] - 1] == color_opp:
                    return False
            if cell[1] + 1 != self.size:
                if field[cell[0]][cell[1] + 1] == color_opp:
                    return False
            return True
        else:
            return False
        return

    def is_looser(self, field, index_player):
        """Перевірити, чи програв гравець"""
        for i in range(self.size):
            for j in range(self.size):
                if not field[i][j] == '-':
                    if field[i][j] == '0':
                        if self.is_move(field, index_player, [i, j]):
                            return False
        return True

    def is_winner(self, field, index_player):
        """Перевірити, чи виграв гравець"""
        index_opp_player = (index_player + 1) % self.players_number
        return self.is_looser(field, index_opp_player)

    def find_best_move(self, field, index_player):
        """Знаходження найкращого ходу"""
        scores = {}
        is_max = self.players[index_player].is_max
        indexes = [[i, j] for i in range(self.size) for j in range(self.size)]
        random.shuffle(indexes)
        for i, j in indexes:
            if field[i][j] == '0':
                if self.is_move(field, index_player, [i, j]):
                    field[i][j] = self.players[index_player].color
                    move_score = self.alpha_beta_prunning(field, 0, not is_max, -float('inf'), float('inf'))
                    field[i][j] = '0'
                    scores[i, j] = move_score
        move = None
        score = None
        if self.game_mode == 'easy':
            if is_max:
                score = float('inf')
                for i in scores.keys():
                    if scores[i] < score:
                        score = scores[i]
                        move = i
            else:
                score = -float('inf')
                for i in scores.keys():
                    if scores[i] > score:
                        score = scores[i]
                        move = i
        elif self.game_mode == 'medium':
            values_sum = 0
            for i in scores.values():
                values_sum += i
            average_value = values_sum // len(scores.values())
            difference = float('inf')
            for i in scores.keys():
                if abs(scores[i] - average_value) < difference:
                    difference = abs(scores[i] - average_value)
                    move = i
                    score = scores[i]
            if not move:
                move = random.choice(scores.keys())
                score = scores[move]
        elif self.game_mode == 'hard':
            if is_max:
                score = -float('inf')
                for i in scores.keys():
                    if scores[i] > score:
                        score = scores[i]
                        move = i
            else:
                score = float('inf')
                for i in scores.keys():
                    if scores[i] < score:
                        score = scores[i]
                        move = i

        return score, move

    def alpha_beta_prunning(self, field, depth, is_max, alpha, beta):
        """Альфа-бета відсікання"""
        index_player = 0
        if self.players[index_player].is_max != is_max:
            index_player = 1
        result = self.is_looser(field, index_player)

        if result:
            if is_max:
                return self.min_score + depth
            else:
                return self.max_score - depth

        if is_max:
            best_score = -float('inf')
            indexes = [[i, j] for i in range(self.size) for j in range(self.size)]
            random.shuffle(indexes)
            for i, j in indexes:
                if field[i][j] == '0':
                    if self.is_move(field, index_player, [i, j]):
                        field[i][j] = self.players[index_player].color
                        best_score = max(best_score, self.alpha_beta_prunning(field, depth + 1, not is_max, alpha, beta))
                        field[i][j] = '0'
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            indexes = [[i, j] for i in range(self.size) for j in range(self.size)]
            random.shuffle(indexes)
            for i, j in indexes:
                if field[i][j] == '0':
                    if self.is_move(field, index_player, [i, j]):
                        field[i][j] = self.players[index_player].color
                        best_score = min(best_score, self.alpha_beta_prunning(field, depth + 1, not is_max, alpha, beta))
                        field[i][j] = '0'
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score
        return

def main():
    """Початок гри"""
    game = Game(GAME_FIELD, COLORS, GAME_MODES[2])

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
                if game.is_winner(game.game_field, game.index_current_player):
                    game.winner = game.players[game.index_current_player]
                    game.output()
                    print('\033[47m\033[90m', 'The winnner is: ', game.winner.name, ' (color: ', game.winner.color, ')', '\033[00m', sep='')
                    break
                game.set_next_player()
        else:
            time_start = time.time_ns()
            best_score, best_move = game.find_best_move(game.game_field, game.index_current_player)
            time_end = time.time_ns()
            print('Score for PC: ', best_score, '  Time in miliseconds:', (time_end-time_start) / 1000 / 1000)
            game.set_cell([best_move[0], best_move[1]], game.players[game.index_current_player].color)
            if game.is_winner(game.game_field, game.index_current_player):
                game.winner = game.players[game.index_current_player]
                game.output()
                print('\033[47m\033[90m', 'The winnner is: ', game.winner.name, ' (color: ', game.winner.color, ')', '\033[00m', sep='')
                break
            game.set_next_player()
    return

if __name__ == "__main__":
    main()