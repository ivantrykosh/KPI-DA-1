# import pygame
#
# pygame.init()
# size = w, h = 500, 400
# main_surface = pygame.display.set_mode((size))
# pygame.display.set_caption("Snort")
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 20)
#
#
# class Label:
#     def __init__(self, text, x, y):
#         self.x = x
#         self.y = y
#         self.set(text, 'white')
#
#     def set(self, text, color):
#         self.text = font.render(text, 1, pygame.Color('white'))
#         size = w, h = self.text.get_size()
#         self.rect = pygame.Rect(self.x, self.y, w, h)
#         self.surface = pygame.Surface(size)
#         self.surface.fill((color))
#         self.surface.blit(self.text, (0, 0))
#
#
# lab1 = Label('   ', 0, 0)
#
#
# def main():
#     loop = 1
#     while loop:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 loop = 0
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if pygame.mouse.get_pressed()[0]:
#                     mx, my = pygame.mouse.get_pos()
#                     if lab1.rect.collidepoint(mx, my):
#                         lab1.set('   ', 'red')
#
#         main_surface.blit(lab1.surface, (0, 0))
#         pygame.display.update()
#         clock.tick(60)
#     # when press quit button it exit
#     pygame.quit()
#     return
# Винести алгоритм в окремий клас Algorithm - done
# Доробити хід комп'ютера - done
# Покращити якість коду
import tkinter as tk
import tkinter.messagebox
import main as Game
from functools import partial

# GAME = Game.Game(Game.GAME_FIELD, Game.COLORS, Game.GAME_MODES[2])

class Labels_and_Moves():
    """Представлення поля Label"""
    def __init__(self, master, x_s, y_s, game, label):
        """Створити поле Label"""
        self.mainwindow = master
        self.Labels = []
        self.create_labels(x_s, y_s)
        # self.label_frame = tk.Frame(master, width=48, height=48, background=color)
        # self.label_frame.place(x=x, y=y)
        # self.label_frame.bind('<Button-1>', self.change_color)
        # self.row = row
        # self.column = column
        self.game = game
        self.label = label
        return

    def change_color(self, row, column, *args):
        """Змінити колір поля Label"""
        index = row * self.game.size + column
        if not self.game.index_current_player:
            tkinter.messagebox.showerror(title='Snort', message='Зараз ходить ' + self.game.players[self.game.index_current_player].name + '!')
        elif self.game.is_move(self.game.game_field, self.game.index_current_player, [row, column]):
            # self.Labels[index].config(bg=self.game.players[self.game.index_current_player].color)
            self.set_color(row, column, self.game.players[self.game.index_current_player].color)
            self.game.set_cell([row, column], self.game.players[self.game.index_current_player].color)
            # if self.game.is_winner(self.game.game_field, self.game.index_current_player):
            #     self.game.winner = self.game.players[self.game.index_current_player]
            #     tkinter.messagebox.showinfo(title='Snort', message='Переможець - ' + self.game.winner.name + '; колір - ' + self.game.winner.color)
            #     self.mainwindow.destroy()
            #     return
            if self.is_winner():
                return
            self.game.set_next_player()
            self.label.config(text=self.game.players[self.game.index_current_player].name, foreground=self.game.players[self.game.index_current_player].color)
            # algorithm = Game.Algorithm(self.game)
            move = self.game.players[self.game.index_current_player].make_move(self.game, True if not self.game.index_current_player else False)
            if move:
                self.set_color(move[0], move[1], self.game.players[self.game.index_current_player].color)
                self.game.set_cell([move[0], move[1]], self.game.players[self.game.index_current_player].color)
                if self.is_winner():
                    return
                self.game.set_next_player()
                self.label.config(text=self.game.players[self.game.index_current_player].name, foreground=self.game.players[self.game.index_current_player].color)
            else:
                return
        else:
            tkinter.messagebox.showerror(title='Snort', message='У цю клітинку походити неможливо!')
        return

    def is_winner(self):
        """Якщо є переможець, то вивести повідомлення та закрити вікно"""
        if self.game.is_winner(self.game.game_field, self.game.index_current_player):
            self.game.winner = self.game.players[self.game.index_current_player]
            tkinter.messagebox.showinfo(title='Snort', message='Переможець - ' + self.game.winner.name + '; колір - ' + self.game.winner.color)
            self.mainwindow.destroy()
            return True
        return False

    def create_labels(self, x_s, y_s):
        row = 0
        column = 0
        for y in y_s:
            for x in x_s:
                color = 'black' if (x == x_s[0] or x == x_s[-1]) and (y == y_s[0] or y == y_s[-1]) else 'white'
                # self.Labels += [Label_and_Move(self.master, x, y, color, row, column, self.GAME, self.LABEL)]
                label_frame = tk.Frame(self.mainwindow, width=48, height=48, background=color)
                label_frame.place(x=x, y=y)
                # label_frame.bind('<Button-1>', lambda: self.change_color(row, column))
                label_frame.bind('<Button-1>', partial(self.change_color, row, column))
                self.Labels += [label_frame]
                column += 1
            row += 1
            column = 0
        return

    def set_color(self, i, j, color):
        index = i * self.game.size + j
        self.Labels[index].config(bg=color)
        return

class BoardWindow():
    """Вікно з ігровим полем"""
    def __init__(self, master):
        """Створити вікно"""
        self.master = master
        self.master.title('Snort')
        self.master.geometry('300x300+475+190')
        self.master.resizable(width=False, height=False)
        # self.master.iconbitmap("icons/logo.ico")

        self.GAME = Game.Game(Game.GAME_FIELD, Game.COLORS, Game.GAME_MODES[2])

        self.create_lines()
        self.LABEL = tk.Label(self.master, text=self.GAME.players[self.GAME.index_current_player].name, foreground=self.GAME.players[self.GAME.index_current_player].color, font=("Helvetica", 18))
        self.LABEL.place(relx=0.5, y=25, anchor='center')
        self.Labels = []
        self.create_labels()

        # await self.make_moves()
        move = self.GAME.players[self.GAME.index_current_player].make_move(self.GAME, True if not self.GAME.index_current_player else False)
        if move:
            self.Labels.set_color(move[0], move[1], self.GAME.players[self.GAME.index_current_player].color)
            self.GAME.set_cell([move[0], move[1]], self.GAME.players[self.GAME.index_current_player].color)
            if self.GAME.is_winner(self.GAME.game_field, self.GAME.index_current_player):
                self.GAME.winner = self.GAME.players[self.GAME.index_current_player]
                tkinter.messagebox.showinfo(title='Snort', message='Переможець - ' + self.GAME.winner.name + '; колір - ' + self.GAME.winner.color)
                self.exit()
            self.GAME.set_next_player()

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
        # self.Labels = []
        # for i in range(self.game.size ** 2):
        #     color = 'white' if not (i == 0 or i == 3 or i == 12 or i == 15) else 'black'
        #     label_frame = tk.Frame(self.master, width=48, height=48, background='red')
        #     # label_frame.pack_propagate(0)
        #     # self.Labels += [[label_frame, tk.Label(label_frame, background=color)]]
        #     self.Labels += [label_frame]

        # self.Labels[0].place(x=37.5, y=57.5)
        # self.Labels[0][0].place(x=37.5, y=57.5)
        # self.Labels[1][0].place(x=90.5, y=57.5)
        x_s = [46.5, 99.5, 152.5, 205.5]
        y_s = [57.5, 110.5, 163.5, 216.5]

        self.Labels = Labels_and_Moves(self.master, x_s, y_s, self.GAME, self.LABEL)
        # self.Labels += [Label(self.master, 46.5, 57.5, False)]
        # self.Labels[0].place(x=46.5, y=57.5)
        # self.Labels += [Label(self.master, 99.5, 57.5, True)]
        # self.Labels[1].place(x=99.5, y=57.5)
        # self.Labels += [Label(self.master, 152.5, 57.5, True)]
        # self.Labels[2].place(x=152.5, y=57.5)
        # self.Labels += [Label(self.master, 205.5, 57.5, False)]
        # self.Labels[3].place(x=205.5, y=57.5)

        # self.Labels += [Label(self.master, 46.5, 110.5, True)]
        # self.Labels[4].place(x=46.5, y=110.5)
        # self.Labels += [Label(self.master, 99.5, 110.5, True)]
        # self.Labels[5].place(x=99.5, y=110.5)
        # self.Labels += [Label(self.master, 152.5, 110.5, True)]
        # self.Labels[6].place(x=152.5, y=110.5)
        # self.Labels += [Label(self.master, 205.5, 110.5, True)]
        # self.Labels[7].place(x=205.5, y=110.5)

        # self.Labels += [Label(self.master, 46.5, 163.5, True)]
        # self.Labels[8].place(x=46.5, y=163.5)
        # self.Labels += [Label(self.master, 99.5, 163.5, True)]
        # self.Labels[9].place(x=99.5, y=163.5)
        # self.Labels += [Label(self.master, 152.5, 163.5, True)]
        # self.Labels[10].place(x=152.5, y=163.5)
        # self.Labels += [Label(self.master, 205.5, 163.5, True)]
        # self.Labels[11].place(x=205.5, y=163.5)

        # self.Labels += [Label(self.master, 46.5, 216.5, False)]
        # self.Labels[12].place(x=46.5, y=216.5)
        # self.Labels += [Label(self.master, 99.5, 216.5, True)]
        # self.Labels[13].place(x=99.5, y=216.5)
        # self.Labels += [Label(self.master, 152.5, 216.5, True)]
        # self.Labels[14].place(x=152.5, y=216.5)
        # self.Labels += [Label(self.master, 205.5, 216.5, False)]
        # self.Labels[15].place(x=205.5, y=216.5)

        # self.Labels[1][0].bind('<Button-1>', self.prep)
        # self.Labels[1].bind('<Button-1>', self.prep)
        return

    async def make_moves(self):
        await self
        while True:
            if not self.GAME.index_current_player:
                move = self.GAME.players[self.GAME.index_current_player].make_move(self.GAME, True)
                if move:
                    self.Labels.set_color(move[0], move[1], self.GAME.players[self.GAME.index_current_player].color)
                    self.GAME.set_cell([move[0], move[1]], self.GAME.players[self.GAME.index_current_player].color)
                    if self.GAME.is_winner(self.GAME.game_field, self.GAME.index_current_player):
                        self.GAME.winner = self.GAME.players[self.GAME.index_current_player]
                        tkinter.messagebox.showinfo(title='Snort', message='Переможець - ' + self.GAME.winner.name + '; колір - ' + self.GAME.winner.color)
                        self.exit()
                        break
                    self.GAME.set_next_player()
                    self.LABEL.config(text=self.GAME.players[self.GAME.index_current_player].name, foreground=self.GAME.players[self.GAME.index_current_player].color)
        return

    def exit(self):
        """Закрити вікно"""
        self.master.destroy()
        return

def main():
    window = tk.Tk()
    app = BoardWindow(window)
    window.mainloop()
    return

if __name__ == '__main__':
    main()