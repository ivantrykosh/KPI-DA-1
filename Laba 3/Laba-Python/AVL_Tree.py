class TreeNode:
    """Вузол дерева"""
    def __init__(self, key, data):
        """Конструктор"""
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        return

class AVL_Tree:
    """АВЛ дерево"""
    def insert(self, node, key, data):
        """Вставка вузла в дерево"""
        if not node:
            return TreeNode(key, data)
        elif key < node.key:
            node.left = self.insert(node.left, key, data)
        elif key > node.key:
            node.right = self.insert(node.right, key, data)
        else:
            print("Error: the keys are the same!")
            return TreeNode(-1, "")
        node.height = 1 + (self.get_height(node.left) if self.get_height(node.left) > self.get_height(node.right) else self.get_height(node.right))
        node = self.balance(node)
        return node

    def balance(self, node):
        """Балансування дерева"""
        Balance = self.get_balance(node)

        if Balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        if Balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        if Balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if Balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def left_rotate(self, node):
        """Поворот ліворуч"""
        node_right = node.right
        node_right__left = node_right.left

        node_right.left = node
        node.right = node_right__left

        node.height = 1 + (self.get_height(node.left) if self.get_height(node.left) > self.get_height(node.right) else self.get_height(node.right))
        node_right.height = 1 + (self.get_height(node_right.left) if self.get_height(node_right.left) > self.get_height(node_right.right) else self.get_height(node_right.right))
        return node_right

    def right_rotate(self, node):
        """Поворот праворуч"""
        node_left = node.left
        node_left__right = node_left.right

        node_left.right = node
        node.left = node_left__right

        node.height = 1 + (self.get_height(node.left) if self.get_height(node.left) > self.get_height(node.right) else self.get_height(node.right))
        node_left.height = 1 + (self.get_height(node_left.left) if self.get_height(node_left.left) > self.get_height(node_left.right) else self.get_height(node_left.right))
        return node_left

    def get_height(self, node):
        """Висота вузла"""
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """Баланс вузла"""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_node(self, node):
        """Мінімальне значення в піддереві"""
        if not node or not node.left:
            return node
        return self.get_min_node(node.left)

    def get_max_node(self, node):
        """Максимальне значення в піддереві"""
        if not node or not node.right:
            return node
        return self.get_max_node(node.right)

    def delete(self, node, key):
        """Видалення елемента за ключем"""
        if not node:
            return node
        elif key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp

            if self.get_balance(node) < 0:
                temp = self.get_min_node(node.right)
                node.key, node.data = temp.key, temp.data
                node.right = self.delete(node.right, node.key)
            elif self.get_balance(node) > 0:
                temp = self.get_max_node(node.left)
                node.key, node.data = temp.key, temp.data
                node.left = self.delete(node.left, node.key)
            else:
                if node.key - node.left.key < node.right.key - node.key:
                    temp = self.get_max_node(node.left)
                    node.key, node.data = temp.key, temp.data
                    node.left = self.delete(node.left, node.key)
                else:
                    temp = self.get_min_node(node.right)
                    node.key, node.data = temp.key, temp.data
                    node.right = self.delete(node.right, node.key)

        if not node:
            return node
        node.height = 1 + (self.get_height(node.left) if self.get_height(node.left) > self.get_height(node.right) else self.get_height(node.right))
        node = self.balance(node)
        return node

    def change_node(self, node, key, new_data):
        """Зміна даних за ключем"""
        if not node:
            return
        elif key < node.key:
            self.change_node(node.left, key, new_data)
        elif key > node.key:
            self.change_node(node.right, key, new_data)
        else:
            node.data = new_data
        return

    def search_node(self, node, key):
        """Пошук даних за ключем"""
        data = None
        if not node:
            return data
        elif key < node.key:
            data = self.search_node(node.left, key)
        elif key > node.key:
            data = self.search_node(node.right, key)
        else:
            return node.data
        return data

    def Print(self, node):
        """Вивід дерева"""
        if not node:
            return

        print(node.key, node.data,  end="\n")
        self.Print(node.left)
        self.Print(node.right)
        return

    def read_data(self, node, path):
        """Читання даних з файлу"""
        with open(path, "r") as file:
            for line in file:
                line = line[:-1] if line[-1] == "\n" else line
                data = line.split()
                int(data[0])
                node = self.insert(node, data[0], data[1])
        return node

    def write_data(self, node, path):
        """Запис даних у файл"""
        with open(path, "w") as file:
            self.traversal(node, file)
        return

    def traversal(self, node, file):
        """Обхід дерева і запис даних у файл"""
        if not node:
            return
        file.write(str(node.key) + " " + node.data + "\n")
        self.traversal(node.left, file)
        self.traversal(node.right, file)
        return