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
    def insert_node(self, node, key, data):
        """Вставка вузла в дерево"""
        is_insert = True
        if not node:
            return TreeNode(key, data), is_insert
        elif key < node.key:
            node.left, is_insert = self.insert_node(node.left, key, data)
        elif key > node.key:
            node.right, is_insert = self.insert_node(node.right, key, data)
        else:
            is_insert = False
            return node, is_insert
        node.height = 1 + (self.get_height(node.left) if self.get_height(node.left) > self.get_height(node.right) else self.get_height(node.right))
        node = self.balance(node)
        return node, is_insert

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

    def delete_node(self, node, key):
        """Видалення елемента за ключем"""
        data = None
        if not node:
            return node, data
        elif key < node.key:
            node.left, data = self.delete_node(node.left, key)
        elif key > node.key:
            node.right, data = self.delete_node(node.right, key)
        else:
            if not node.left:
                temp = node.right
                data = node.data
                node = None
                return temp, data
            elif not node.right:
                temp = node.left
                node = None
                return temp, data

            if self.get_balance(node) < 0:
                temp = self.get_min_node(node.right)
                node.key, node.data = temp.key, temp.data
                node.right, data = self.delete_node(node.right, node.key)
            elif self.get_balance(node) > 0:
                temp = self.get_max_node(node.left)
                node.key, node.data = temp.key, temp.data
                node.left, data = self.delete_node(node.left, node.key)
            else:
                if node.key - node.left.key < node.right.key - node.key:
                    temp = self.get_max_node(node.left)
                    node.key, node.data = temp.key, temp.data
                    node.left, data = self.delete_node(node.left, node.key)
                else:
                    temp = self.get_min_node(node.right)
                    node.key, node.data = temp.key, temp.data
                    node.right, data = self.delete_node(node.right, node.key)

        if not node:
            return node, data
        node.height = 1 + (self.get_height(node.left) if self.get_height(node.left) > self.get_height(node.right) else self.get_height(node.right))
        node = self.balance(node)
        return node, data

    def change_node(self, node, key, new_data):
        """Зміна даних за ключем"""
        is_change = True
        if not node:
            is_change = False
            return node, is_change
        elif key < node.key:
            node.left, is_change = self.change_node(node.left, key, new_data)
        elif key > node.key:
            node.right, is_change = self.change_node(node.right, key, new_data)
        else:
            node.data = new_data
        return node, is_change

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
                data[0] = int(data[0])
                node, temp = self.insert_node(node, data[0], data[1])
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