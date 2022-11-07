import AVL_Tree
import tkinter as tk
import tkinter.filedialog

class Window1:
    """Початкове вікно"""
    def __init__(self, master):
        """Створення вікна"""
        self.master = master
        self.master.title("СУБД")
        self.master.geometry("300x200")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("logo.ico")

        self.label = tk.Label(text="Оберіть дію:", background="#d3d3d3", font=("Arial, 13"))
        self.label.pack(pady=5)
        self.button3 = tk.Button(text="Вийти", font=("Arial, 10"), width=5, height=1, background="#d3d3d3", command=self.exit)
        self.button3.place(x=245, y=5)
        self.button1 = tk.Button(text="Створити базу даних", font=("Arial, 10"), width=20, height=3, background="#d3d3d3", command=self.create_DB)
        self.button1.pack(pady=10)
        self.button2 = tk.Button(text="Обрати базу даних", font=("Arial, 10"), width=20, height=3, background="#d3d3d3", command=self.open_file)
        self.button2.pack(pady=10)

    # def new_window(self):
    #     self.newWindow = tk.Toplevel(self.master)
    #     self.app = Window2(self.newWindow)

    def open_file(self):
        """Відкрити шлях до файлу"""
        filepath = tk.filedialog.askopenfilename()
        self.Tree = AVL_Tree.AVL_Tree()
        self.root = None
        self.root = self.Tree.read_data(self.root, filepath)
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow, self.master, self.Tree, self.root)
        return

    def exit(self):
        """Закрити вікно"""
        self.master.destroy()
        return

    def create_DB(self):
        """Створення бази даних"""
        self.Tree = AVL_Tree.AVL_Tree()
        self.root = None
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow, self.master, self.Tree, self.root)
        return

class Window2:
    def __init__(self, master, mainwindow, Tree, root):
        self.mainwindow = mainwindow
        self.Tree = Tree
        self.root = root

        self.master = master
        self.master.title("СУБД")
        self.master.geometry("320x240")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("logo.ico")

        self.label = tk.Label(self.master,text="Оберіть дію:", background="#d3d3d3", height=2, font=("Arial, 13"))
        self.label.pack(pady=5)
        self.button1 = tk.Button(self.master, text="Головне\nменю", font=("Arial, 8"), width=12, height=2, background="#d3d3d3", command=self.close_window)
        self.button1.place(x=232, y=5)
        self.button2 = tk.Button(self.master, text="Знайти запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3")
        self.button2.place(x=15, y=65)
        self.button3 = tk.Button(self.master, text="Додати запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3")
        self.button3.place(x=172, y=65)
        self.button4 = tk.Button(self.master, text="Видалити запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3")
        self.button4.place(x=15, y=125)
        self.button5 = tk.Button(self.master, text="Змінити запис", font=("Arial, 10"), width=15, height=2, background="#d3d3d3")
        self.button5.place(x=172, y=125)
        self.button6 = tk.Button(self.master, text="Зберегти", font=("Arial, 10"), width=35, height=2, background="#d3d3d3")
        self.button6.place(x=13, y=185)

    def close_window(self):
        self.master.destroy()
        self.mainwindow.deiconify()

def main():

    # window = tk.Tk()
    # window.title("СУБД")
    # window.geometry("300x200")
    # window.iconbitmap("logo.ico")
    #
    # label = tk.Label(text="Оберіть дію:", background="#d3d3d3", font=("Arial, 13"))
    # label.pack(pady=5)
    # button1 = tk.Button(text="Створити базу даних", font=("Arial, 10"), width=20, height=3, background="#d3d3d3")
    # button1.pack(pady=10)
    # button2 = tk.Button(text="Обрати базу даних", font=("Arial, 10"), width=20, height=3, background="#d3d3d3")
    # button2.pack(pady=10)
    #
    # window.mainloop()

    window = tk.Tk()
    app = Window1(window)
    window.mainloop()

    # Tree = AVL_Tree.AVL_Tree()
    # root = None

    # root = Tree.insert(root, 9, "jhdkjaqsl")
    # root = Tree.insert(root, 5, "jhdksjasl")
    # root = Tree.insert(root, 10, "jhdkjafsl")
    # root = Tree.insert(root, 0, "jhadkjasl")
    # root = Tree.insert(root, 6, "jhdakjasl")
    # root = Tree.insert(root, 11, "jhdkfjasl")
    # root = Tree.insert(root, -1, "jhdkfjasl")
    # root = Tree.insert(root, 1, "jhdkfjasl")
    # root = Tree.insert(root, 2, "jhdkfjasl")
    # root = Tree.insert(root, 10, "10jhdkjaqsl")
    # root = Tree.insert(root, 6, "6jhdksjasl")
    # root = Tree.insert(root, 4, "4jhdkjafsl")
    # root = Tree.insert(root, 3, "3jhadkjasl")
    # root = Tree.insert(root, 7, "7jhdakjasl")
    # root = Tree.insert(root, 16, "16jhdkfjasl")
    # root = Tree.insert(root, 12, "12jhdkfjasl")
    # root = Tree.insert(root, 14, "14jhdkfjasl")
    # root = Tree.insert(root, 22, "22jhdkfjasl")
    # root = Tree.insert(root, 19, "19jhdkjaqsl")
    # root = Tree.insert(root, 17, "17jhdksjasl")
    # root = Tree.insert(root, 21, "21jhdkjafsl")
    # root = Tree.insert(root, 24, "24jhadkjasl")

    # Tree.Print(root)

    # root = Tree.Delete(root, 10)
    # root = Tree.delete(root, 10)
    # print()
    # Tree.Print(root)

    # Tree.change_node(root, 24, "24qwerytuiopuytrtyuiop")
    # print()
    # Tree.Print(root)

    # data = Tree.search_node(root, 3)
    # print(3, data)

    return

if __name__ == "__main__":
    main()
