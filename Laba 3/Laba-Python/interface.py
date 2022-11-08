import AVL_Tree
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from random import shuffle

class Window1:
    """Початкове вікно"""
    def __init__(self, master):
        """Створення вікна"""
        self.master = master
        self.master.title("СУБД")
        self.master.geometry("300x200")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("icons/logo.ico")

        self.label = tk.Label(text="Оберіть дію:", background="#d3d3d3", font=("Arial, 13"))
        self.label.pack(pady=5)
        self.button3 = tk.Button(text="Вийти", font=("Arial, 10"), width=5, height=1, background="#d3d3d3", command=self.exit)
        self.button3.place(x=245, y=5)
        self.button1 = tk.Button(text="Створити базу даних", font=("Arial, 10"), width=20, height=3, background="#d3d3d3", command=self.create_DB)
        self.button1.pack(pady=10)
        self.button2 = tk.Button(text="Обрати базу даних", font=("Arial, 10"), width=20, height=3, background="#d3d3d3", command=self.open_file)
        self.button2.pack(pady=10)

        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        return

    def open_file(self):
        """Відкрити шлях до файлу БД і відкрити нове вікно"""
        filepath = tk.filedialog.askopenfilename(title="Відкрити базу даних", initialdir="C:/Ivan/DA-Labs/Laba 3", defaultextension=".txt",filetypes=[("Бази даних","*.txt")])
        if not filepath:
            tkinter.messagebox.showerror(title="СУБД", message="Файл не вибрано!")
        else:
            self.master.withdraw()
            self.newWindow = tk.Toplevel(self.master)
            self.app = Window2(self.newWindow, self.master, filepath)
        return

    def exit(self):
        """Закрити вікно"""
        self.master.destroy()
        return

    def create_DB(self):
        """Створити базу даних і відкрити нове вікно"""
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow, self.master, None)
        return

class Window2:
    """Вікно з функціями додавання, пошуку, видалення та зміни запису"""
    def __init__(self, master, mainwindow, filepath):
        """Створення вікна"""
        self.mainwindow = mainwindow
        self.app = None
        self.master = master
        try:
            self.Tree = AVL_Tree.AVL_Tree()
            self.root = None
            self.root = self.Tree.read_data(self.root, filepath) if filepath else None
            self.filepath = filepath

            self.master.title("СУБД")
            self.master.geometry("320x240")
            self.master.resizable(width=False, height=False)
            self.master.iconbitmap("icons/logo.ico")

            self.label = tk.Label(self.master,text="Оберіть дію:", background="#d3d3d3", height=2, font=("Arial, 13"))
            self.label.pack(pady=5)
            self.button1 = tk.Button(self.master, text="Головне\nменю", font=("Arial, 8"), width=12, height=2, background="#d3d3d3", command=self.close_window)
            self.button1.place(x=232, y=5)
            self.button2 = tk.Button(self.master, text="Знайти запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.search_record)
            self.button2.place(x=15, y=65)
            self.button3 = tk.Button(self.master, text="Додати запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.insert_record)
            self.button3.place(x=172, y=65)
            self.button4 = tk.Button(self.master, text="Видалити запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.delete_record)
            self.button4.place(x=15, y=125)
            self.button5 = tk.Button(self.master, text="Змінити запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.change_record)
            self.button5.place(x=172, y=125)
            self.button6 = tk.Button(self.master, text="Зберегти", font=("Arial, 10"), width=35, height=2, background="#d3d3d3", command=self.save_DB)
            self.button6.place(x=13, y=185)

            self.master.protocol("WM_DELETE_WINDOW", self.close_window)
        except ValueError:
            tkinter.messagebox.showerror(title="СУБД", message="Помилка при зчитуванні файлу!")
            self.mainwindow.deiconify()
            self.master.destroy()
        return

    def close_window(self):
        """Закрити вікно редагування БД і відкрити головне вікно"""
        if self.app:
            self.Tree, self.root = self.app.get_tree_root()
        is_save = True
        if tkinter.messagebox.askyesno(title="СУБД", message="Зберегти базу даних?"):
            is_save = self.save_DB()
        if is_save:
            self.mainwindow.deiconify()
            self.master.destroy()
        return

    def save_DB(self):
        """Збереження БД у файл"""
        if self.app:
            self.Tree, self.root = self.app.get_tree_root()
        is_save = True
        if self.filepath:
            self.Tree.write_data(self.root, self.filepath)
        else:
            self.filepath = tk.filedialog.asksaveasfile(title="Зберегти базу даних", initialdir="C:/Ivan/DA-Labs/Laba 3", initialfile = "Untitled.txt", defaultextension=".txt", filetypes=[("Бази даних","*.txt")])
            if not self.filepath:
                tkinter.messagebox.showerror(title="СУБД", message="Файл не вибрано!")
                is_save = False
            else:
                self.filepath = self.filepath.name
                self.Tree.write_data(self.root, self.filepath)
        return is_save

    def search_record(self):
        """Пошук даних за ключем"""
        if self.app:
            self.Tree, self.root = self.app.get_tree_root()
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Search_record(self.newWindow, self.master, self.Tree, self.root)
        return

    def insert_record(self):
        """Додавання даних за ключем"""
        if self.app:
            self.Tree, self.root = self.app.get_tree_root()
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Insert_record(self.newWindow, self.master, self.Tree, self.root)
        return

    def delete_record(self):
        """Видалення даних за ключем"""
        if self.app:
            self.Tree, self.root = self.app.get_tree_root()
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Delete_record(self.newWindow, self.master, self.Tree, self.root)
        return

    def change_record(self):
        """Зміна даних за ключем"""
        if self.app:
            self.Tree, self.root = self.app.get_tree_root()
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Change_record(self.newWindow, self.master, self.Tree, self.root)
        return

class Search_record():
    """Вікно для пошуку запису"""
    def __init__(self, master, previous_window, Tree, root):
        """Конструктор для створення вікна"""
        self.previous_window = previous_window
        self.Tree = Tree
        self.root = root

        self.master = master
        self.master.title("Знайти запис")
        self.master.geometry("300x105")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("icons/logo.ico")

        self.label = tk.Label(self.master, text="Введіть ключ:", background="#d3d3d3", height=1, width=15, font=("Arial, 10"), justify=tk.CENTER)
        self.label.place(x=15, y=15)
        self.entry = tk.Entry(self.master, font=("Arial, 10"), justify=tk.CENTER, width=18)
        self.entry.place(x=155, y=15)
        self.button1 = tk.Button(self.master, text="Знайти запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.search_record)
        self.button1.place(x=13, y=50)
        self.button2 = tk.Button(self.master, text="Скасувати", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.exit)
        self.button2.place(x=155, y=50)

        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        return

    def search_record(self):
        """Знайти запис за ключем"""
        if not self.entry.get():
            tkinter.messagebox.showerror(title="Знайти запис", message="Ключ не введений!")
        else:
            try:
                key = int(self.entry.get())
                data = self.Tree.search_node(self.root, key)
                message = ("Запис знайдено!\nКлюч: " + str(key) + "\nДані: " + str(data)) if data else "Даних за ключем " + str(key) + " не знайдено!"
                tkinter.messagebox.showinfo(title="Знайти запис", message=message)

                print(f"Число порівнянь для знаходження запису за ключем {key} = {self.Tree.number_comparison}")
                self.Tree.number_comparison = 0
            except ValueError:
                tkinter.messagebox.showerror(title="Знайти запис", message="Ключ повинен бути цілим числом!")
        return

    def exit(self):
        """Закрити вікно і відкрити попереднє вікно"""
        self.previous_window.deiconify()
        self.master.destroy()
        return

    def get_tree_root(self):
        """Отримати значення"""
        return self.Tree, self.root

class Insert_record():
    """Вікно для вставки запису"""
    def __init__(self, master, previous_window, Tree, root):
        """Конструктор для створення вікна"""
        self.previous_window = previous_window
        self.Tree = Tree
        self.root = root

        self.master = master
        self.master.title("Вставити запис")
        self.master.geometry("300x140")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("icons/logo.ico")

        self.label1 = tk.Label(self.master, text="Введіть ключ:", background="#d3d3d3", height=1, width=15, font=("Arial, 10"), justify=tk.CENTER)
        self.label1.place(x=15, y=15)
        self.entry1 = tk.Entry(self.master, font=("Arial, 10"), justify=tk.CENTER, width=18)
        self.entry1.place(x=155, y=15)
        self.label2 = tk.Label(self.master, text="Введіть дані:", background="#d3d3d3", height=1, width=15, font=("Arial, 10"), justify=tk.CENTER)
        self.label2.place(x=15, y=50)
        self.entry2 = tk.Entry(self.master, font=("Arial, 10"), justify=tk.CENTER, width=18)
        self.entry2.place(x=155, y=50)
        self.button1 = tk.Button(self.master, text="Вставити запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.insert_record)
        self.button1.place(x=13, y=85)
        self.button2 = tk.Button(self.master, text="Скасувати", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.exit)
        self.button2.place(x=155, y=85)

        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        return

    def insert_record(self):
        """Вставка запису"""
        if not self.entry1.get():
            tkinter.messagebox.showerror(title="Вставити запис", message="Ключ не введений!")
        elif not self.entry2.get():
            tkinter.messagebox.showerror(title="Вставити запис", message="Дані не введені!")
        else:
            try:
                key = int(self.entry1.get())
                data = self.entry2.get()
                node, is_insert = self.Tree.insert_node(self.root, key, data)
                self.root = node if is_insert else self.root
                message = ("Запис вставлено!\nКлюч: " + str(key) + "\nДані: " + str(data)) if is_insert else "Ключ " + str(key) + " вже є у базі даних!"
                tkinter.messagebox.showinfo(title="Вставити запис", message=message)
            except ValueError:
                tkinter.messagebox.showerror(title="Вставити запис", message="Ключ повинен бути цілим числом!")
        return

    def exit(self):
        """Закрити вікно і відкрити попереднє вікно"""
        self.previous_window.deiconify()
        self.master.destroy()
        return

    def get_tree_root(self):
        """Отримати значення"""
        return self.Tree, self.root

class Delete_record():
    """Вікно для видалення запису"""
    def __init__(self, master, previous_window, Tree, root):
        """Конструктор для створення вікна"""
        self.previous_window = previous_window
        self.Tree = Tree
        self.root = root

        self.master = master
        self.master.title("Видалити запис")
        self.master.geometry("300x105")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("icons/logo.ico")

        self.label = tk.Label(self.master, text="Введіть ключ:", background="#d3d3d3", height=1, width=15, font=("Arial, 10"), justify=tk.CENTER)
        self.label.place(x=15, y=15)
        self.entry = tk.Entry(self.master, font=("Arial, 10"), justify=tk.CENTER, width=18)
        self.entry.place(x=155, y=15)
        self.button1 = tk.Button(self.master, text="Видалити запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.delete_record)
        self.button1.place(x=13, y=50)
        self.button2 = tk.Button(self.master, text="Скасувати", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.exit)
        self.button2.place(x=155, y=50)

        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        return

    def delete_record(self):
        """Видалити запис за ключем"""
        if not self.entry.get():
            tkinter.messagebox.showerror(title="Видалення запису", message="Ключ не введений!")
        else:
            try:
                key = int(self.entry.get())
                self.root, data = self.Tree.delete_node(self.root, key)
                message = ("Запис видалено!\nКлюч: " + str(key) + "\nДані: " + str(data)) if data else "Даних за ключем " + str(key) + " немає!"
                tkinter.messagebox.showinfo(title="Видалення запису", message=message)
            except ValueError:
                tkinter.messagebox.showerror(title="Видалення запису", message="Ключ повинен бути цілим числом!")
        return

    def exit(self):
        """Закрити вікно і відкрити попереднє вікно"""
        self.previous_window.deiconify()
        self.master.destroy()
        return

    def get_tree_root(self):
        """Отримати значення"""
        return self.Tree, self.root

class Change_record():
    """Вікно для зміни запису"""
    def __init__(self, master, previous_window, Tree, root):
        """Конструктор для створення вікна"""
        self.previous_window = previous_window
        self.Tree = Tree
        self.root = root

        self.master = master
        self.master.title("Змінити запис")
        self.master.geometry("300x140")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("icons/logo.ico")

        self.label1 = tk.Label(self.master, text="Введіть ключ:", background="#d3d3d3", height=1, width=15, font=("Arial, 10"), justify=tk.CENTER)
        self.label1.place(x=15, y=15)
        self.entry1 = tk.Entry(self.master, font=("Arial, 10"), justify=tk.CENTER, width=18)
        self.entry1.place(x=155, y=15)
        self.label2 = tk.Label(self.master, text="Введіть нові дані:", background="#d3d3d3", height=1, width=15, font=("Arial, 10"), justify=tk.CENTER)
        self.label2.place(x=15, y=50)
        self.entry2 = tk.Entry(self.master, font=("Arial, 10"), justify=tk.CENTER, width=18)
        self.entry2.place(x=155, y=50)
        self.button1 = tk.Button(self.master, text="Змінити запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.change_record)
        self.button1.place(x=13, y=85)
        self.button2 = tk.Button(self.master, text="Скасувати", font=("Arial, 10"), width=15, height=2, background="#d3d3d3", command=self.exit)
        self.button2.place(x=155, y=85)

        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        return

    def change_record(self):
        """Вставка запису"""
        if not self.entry1.get():
            tkinter.messagebox.showerror(title="Змінити запис", message="Ключ не введений!")
        elif not self.entry2.get():
            tkinter.messagebox.showerror(title="Змінити запис", message="Нові дані не введені!")
        else:
            try:
                key = int(self.entry1.get())
                new_data = self.entry2.get()
                self.root, is_change = self.Tree.change_node(self.root, key, new_data)
                message = ("Запис змінено!\nКлюч: " + str(key) + "\nНові дані: " + str(new_data)) if is_change else "Ключа " + str(key) + " немає в базі даних!"
                tkinter.messagebox.showinfo(title="Змінити запис", message=message)
            except ValueError:
                tkinter.messagebox.showerror(title="Змінити запис", message="Ключ повинен бути цілим числом!")
        return

    def exit(self):
        """Закрити вікно і відкрити попереднє вікно"""
        self.previous_window.deiconify()
        self.master.destroy()
        return

    def get_tree_root(self):
        """Отримати значення"""
        return self.Tree, self.root

def main():
    window = tk.Tk()
    app = Window1(window)
    window.mainloop()

    # Tree = AVL_Tree.AVL_Tree()
    # root = None
    #
    # keys = [i for i in range(-5000, 5000)]
    # shuffle(keys)
    # for i in keys:
    #     root, temp = Tree.insert_node(root, i, str(i % 2500))
    #
    # Tree.write_data(root, "C:/Ivan/DA-Labs/Laba 3/DB10000.txt")

    # root, temp = Tree.delete_node(root, )
    # root, temp = Tree.change_node(root, , "")
    # data = Tree.search_node(root, 3)

    return

if __name__ == "__main__":
    main()
