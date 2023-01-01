import tkinter as tk
import tkinter.messagebox
import game as Game
from functools import partial
import constants as const

class Labels_and_Moves():
    """
    Представлення ігрового поля та відтворення ходів гравців

    :param master: вікно з ігровим полем
    :param mainwindow: стартове вікно
    :param Labels: ігрові клітинки
    :param game: об'єкт класу Game.Game
    :param label: поле з ім'ям гравця, що зараз ходить
    """
    def __init__(self, master, mainwindow, x_s, y_s, game, label):
        """Створити ігрові клітинки"""
        self.master = master
        self.mainwindow = mainwindow
        self.Labels = []
        self.create_labels(x_s, y_s)
        self.game = game
        self.label = label
        return

    def make_move_user(self, row, column):
        """Хід користувача"""
        index = row * self.game.size + column
        is_move = False
        if not self.game.index_current_player:
            tkinter.messagebox.showerror(title='Snort', message='Зараз ходить ' + self.game.players[
                self.game.index_current_player].name + '!')
        elif self.game.is_move(self.game.game_field, self.game.index_current_player, [row, column]):
            self.set_color(row, column, self.game.players[self.game.index_current_player].color)
            self.game.set_cell([row, column], self.game.players[self.game.index_current_player].color)
            is_move = True
            if self.is_winner():
                is_move = False
                return is_move
            self.game.set_next_player()
            self.label.config(text=self.game.players[self.game.index_current_player].name,
                              foreground=self.game.players[self.game.index_current_player].color)
        else:
            if self.game.game_field[row][column] != '-':
                tkinter.messagebox.showerror(title='Snort', message='У цю клітинку походити неможливо!')
        return is_move

    def make_move_pc(self):
        """Хід комп'ютера"""
        move = self.game.players[self.game.index_current_player].make_move(self.game, True if not self.game.index_current_player else False)
        if move:
            self.set_color(move[0], move[1], self.game.players[self.game.index_current_player].color)
            self.game.set_cell([move[0], move[1]], self.game.players[self.game.index_current_player].color)
            if self.is_winner():
                return
            self.game.set_next_player()
            self.label.config(text=self.game.players[self.game.index_current_player].name,
                              foreground=self.game.players[self.game.index_current_player].color)
        else:
            return
        return

    def change_color(self, row, column, *args):
        """Змінити колір поля Label (зробити ходи користувача та комп'ютера)"""
        is_move = self.make_move_user(row, column)
        if is_move:
            self.make_move_pc()
            if not self.game.winner:
                self.paint_unmoved_cells()
        return

    def paint_unmoved_cells(self):
        """Зафарбувати клітинки, в які неможна походити"""
        for i in range(self.game.size):
            for j in range(self.game.size):
                if self.game.game_field[i][j] == '0' and not self.game.is_move(self.game.game_field, self.game.index_current_player, [i, j]):
                    self.set_color(i, j, '#B3B1B2')
        return

    def is_winner(self):
        """Якщо є переможець, то вивести повідомлення та закрити вікно"""
        if self.game.is_winner(self.game.game_field, self.game.index_current_player):
            self.game.winner = self.game.players[self.game.index_current_player]
            for i in range(len(self.Labels)):
                self.Labels[i].bind('<Button-1>', partial(self.nothing))
            tkinter.messagebox.showinfo(title='Snort', message='Переможець - ' + self.game.winner.name + '; колір - ' + self.game.winner.color)
            self.mainwindow.deiconify()
            self.master.destroy()
            return True
        return False

    def create_labels(self, x_s, y_s):
        """Створити поле гри"""
        row = 0
        column = 0
        for y in y_s:
            for x in x_s:
                color = 'black' if (x == x_s[0] or x == x_s[-1]) and (y == y_s[0] or y == y_s[-1]) else 'white'
                label_frame = tk.Frame(self.master, width=48, height=48, background=color)
                label_frame.place(x=x, y=y)
                label_frame.bind('<Button-1>', partial(self.change_color, row, column))
                self.Labels += [label_frame]
                column += 1
            row += 1
            column = 0
        return

    def set_color(self, i, j, color):
        """Змінити колір клітинки"""
        index = i * self.game.size + j
        self.Labels[index].config(bg=color)
        return

    def nothing(self, *args):
        """Пустий метод (для того, щоб зміна кольору не відбувалась після завершення гри"""
        return

class BoardWindow():
    """
    Вікно з ігровим полем

    :param master: вікно з ігровим полем
    :param mainwindow: початкове вікно
    :param game_mode: режим гри
    :param game_field: ігрове поле
    :param GAME: об'єкт класу Game.Game
    :param LABEL: поле з ім'ям поточного гравця
    :param Labels: ігрове поле
    """
    def __init__(self, master, mainwindow, game_mode):
        """Створити вікно"""
        self.master = master
        self.master.title('Snort')
        self.master.geometry('300x300+475+190')
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("icons/icon.ico")
        self.mainwindow = mainwindow

        self.game_mode = game_mode
        self.game_field = []
        for i in range(len(const.GAME_FIELD)):
            temp = []
            for j in range(len(const.GAME_FIELD[i])):
                temp += [const.GAME_FIELD[i][j]]
            self.game_field += [temp]
        self.GAME = Game.Game(self.game_field, const.COLORS, self.game_mode)

        self.create_lines()
        self.LABEL = tk.Label(self.master, text=self.GAME.players[self.GAME.index_current_player].name, foreground=self.GAME.players[self.GAME.index_current_player].color, font=("Helvetica", 18))
        self.LABEL.place(relx=0.5, y=25, anchor='center')
        self.Labels = None
        self.create_labels()

        self.Labels.make_move_pc()
        if not self.GAME.winner:
            self.Labels.paint_unmoved_cells()

        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        return

    def create_lines(self):
        """Створення ліній"""
        canvas = tk.Canvas(self.master)
        canvas.create_line(46.5, 107.5, 253.5, 107.5, width=5)
        canvas.create_line(46.5, 160.5, 253.5, 160.5, width=5)
        canvas.create_line(46.5, 213.5, 253.5, 213.5, width=5)

        canvas.create_line(96.5, 57.5, 96.5, 264.5, width=5)
        canvas.create_line(149.5, 57.5, 149.5, 264.5, width=5)
        canvas.create_line(202.5, 57.5, 202.5, 264.5, width=5)
        canvas.pack()
        return

    def create_labels(self):
        """Створення клітинок"""
        x_s = [46.5, 99.5, 152.5, 205.5]
        y_s = [57.5, 110.5, 163.5, 216.5]
        self.Labels = Labels_and_Moves(self.master, self.mainwindow, x_s, y_s, self.GAME, self.LABEL)
        return

    def exit(self):
        """Закрити вікно"""
        self.mainwindow.deiconify()
        self.master.destroy()
        return

class Game_modes():
    """
    Вікно з вибором ігрового режиму

    :param master: поточне вікно
    :param mainwindow: початкове вікно
    :param app: вікно з ігровим полем
    :param game_mode: обраний режим гри
    """
    def __init__(self, master, mainwindow):
        """Створення вікна та кнопок"""
        self.master = master
        self.mainwindow = mainwindow
        self.app = None

        self.master.title('Snort')
        self.master.geometry('300x300+475+190')
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("icons/icon.ico")
        self.master.config(background='#616161')

        self.game_mode = None

        self.label = tk.Label(self.master, text='ОБЕРІТЬ РЕЖИМ ГРИ', background='#d3d3d3', font=('Times, 15'))
        self.label.place(x=40, y=20, width=220, height=30)
        self.button1 = tk.Button(self.master, text='ЛЕГКИЙ', font=('Times, 15'), background='#d3d3d3', command=lambda: self.set_game_mode(0))
        self.button1.place(x=90, y=70, width=120, height=40)
        self.button2 = tk.Button(self.master, text='СЕРЕДНІЙ', font=('Times, 15'), background='#d3d3d3', command=lambda: self.set_game_mode(1))
        self.button2.place(x=90, y=120, width=120, height=40)
        self.button3 = tk.Button(self.master, text='ВАЖКИЙ', font=('Times, 15'), background='#d3d3d3', command=lambda: self.set_game_mode(2))
        self.button3.place(x=90, y=170, width=120, height=40)
        self.button4 = tk.Button(self.master, text='НАЗАД', font=('Times, 15'), background='#d3d3d3', command=self.close_window)
        self.button4.place(x=90, y=240, width=120, height=40)

        self.master.protocol("WM_DELETE_WINDOW", self.close_window)
        return

    def set_game_mode(self, index, *args):
        """Встановлення ігрового режиму"""
        if 0 <= index < len(const.GAME_MODES):
            self.game_mode = const.GAME_MODES[index]
            self.start_game()
        return

    def start_game(self):
        """Початок гри (запуск вікна з ігровим полем)"""
        if self.game_mode:
            self.master.withdraw()
            self.newWindow = tk.Toplevel(self.master)
            self.app = BoardWindow(self.newWindow, self.mainwindow, self.game_mode)
        return

    def close_window(self):
        """Закрити вікно"""
        self.mainwindow.deiconify()
        self.master.destroy()
        return

class MainMenu():
    """
    Головне меню

    :param master: поточне вікно
    :param app: вікно з вибором ігрового режиму
    """
    def __init__(self, master):
        """Створення вікна"""
        self.master = master
        self.app = None

        self.master.title('Snort')
        self.master.geometry('300x300+475+190')
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("icons/icon.ico")
        self.master.config(background='#616161')

        self.label = tk.Label(self.master, text='SNORT', background='#d3d3d3', font=('Arial, 20'))
        self.label.place(x=85, y=30, width=130, height=60)
        self.button1 = tk.Button(self.master, text='ГРАТИ', font=('Arial, 15'), background='#d3d3d3', command=self.choose_game_mode)
        self.button1.place(x=85, y=130, width=130, height=60)
        self.button2 = tk.Button(self.master, text='ВИЙТИ', font=('Arial, 15'), background='#d3d3d3', command=self.exit)
        self.button2.place(x=85, y=210, width=130, height=60)

        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        return

    def choose_game_mode(self):
        """Створення вікна з вибором ігрового режиму"""
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Game_modes(self.newWindow, self.master)
        return

    def exit(self):
        """Закрити вікно"""
        self.master.destroy()
        return

def main():
    """Початок програми"""
    window = tk.Tk()
    app = MainMenu(window)
    window.mainloop()
    return

if __name__ == '__main__':
    main()