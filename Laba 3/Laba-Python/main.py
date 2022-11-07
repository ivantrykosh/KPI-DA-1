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
        # node = self.balance(node)
        return node

    def balance(self, node):
        """Балансування дерева"""
        Balance = self.get_balance(node)

        #     # Case 1 - Right Right
        # if balance > 1 and key < root.left.key:
        #     return self.rightRotate(root)
        #
        #     # Case 2 - Left Left
        # if balance < -1 and key > root.right.key:
        #     return self.leftRotate(root)
        #
        #     # Case 3 - Left Right
        # if balance > 1 and key > root.left.key:
        #     root.left = self.leftRotate(root.left)
        #     return self.rightRotate(root)
        #
        #     # Case 4 - Right Left
        # if balance < -1 and key < root.right.key:
        #     root.right = self.rightRotate(root.right)
        #     return self.leftRotate(root)

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

    def delete_node(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            # queue = self.get_min_key(node, [])
            self.replace_delete_key(node)
            self.reset_heights(node)
            # temp = node
            # node = min_node
            # min_node = temp
        # Зробити get_min_key рекурсією для видалення вузла node. 6 лаба з АСД-2


        return

    # def get_min_key(self, node, queue):
    def replace_delete_key(self, node):
        """Заміна найближчого до ключа значення і видалення ключа"""
        # if not node:
        #     return queue
        # elif self.get_balance(node) < 0:
        #     self.get_balance(node.right)
        # elif self.get_balance(node) > 0:
        #     self.get_balance(node.right)
        # else:
        #     if self.get_balance(node.left) < self.get_balance(node.right):
        #         self.get_min_key(node.left)
        #     else:
        #         self.get_min_key(node.right)
        temp = None
        if not node:
            return node
        elif self.get_balance(node) < 0:
            # temp = node.right
            # while temp.left:
            #     temp = temp.left
            temp = self.get_min_node(node)
            # return temp
        elif self.get_balance(node) > 0:
            # temp = node.left
            # while temp.right:
            #     temp = temp.right
            temp = self.get_max_node(node)
            # return temp
        else:
            if node.key - node.left.key < node.right.key - node.key:
                # temp = node.left
                # while temp.right:
                #     temp = temp.right
                temp = self.get_max_node(node)
                # return temp
            else:
                # temp = node.right
                # while temp.left:
                #     temp = temp.left
                temp = self.get_min_node(node)
                # return temp
        # Node_temp = node
        # node = temp
        # temp = Node_temp

        node, temp = temp, node

        # node.height = 1 + (self.get_height(node.left) if self.get_height(node.left) > self.get_height(node.right) else self.get_height(node.right))
        # temp.height = 1 + (self.get_height(temp.left) if self.get_height(temp.left) > self.get_height(temp.right) else self.get_height(temp.right))
        if node.left or node.right:
            self.replace_delete_key(node)
        # else:
        #     node = None
        return temp

    def get_min_node(self, node):
        """Мінімальне значення в піддереві"""
        if not node or not node.left:
            return node
        return self.get_min_node(node.left)

    def get_max_node(self, node):
        """Максимальне значення в піддереві"""
        if not node or not node.right:
            return node
        return self.get_min_node(node.right)

    def reset_heights(self, node):
        """Перевизначення висот"""
        if not node:
            return
        self.reset_heights(node.left)
        self.reset_heights(node.right)
        node.height = 1 + (self.get_height(node.left) if self.get_height(node.left) > self.get_height(node.right) else self.get_height(node.right))
        return

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
        # node = self.balance(node)
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

    def Delete(self, root, key):
        # Step 1 - Perform standard BST delete
        if not root:
            return root
        elif key < root.key:
            root.left = self.Delete(root.left, key)
        elif key > root.key:
            root.right = self.Delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_node(root.right)
            root.key, root.data = temp.key, temp.data
            root.right = self.Delete(root.right, temp.key)

        # If the tree has only one node,
        # simply return it
        if root is None:
            return root

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + (self.get_height(root.left) if self.get_height(root.left) > self.get_height(root.right) else self.get_height(root.right))

        root = self.balance(root)
        return root

    def DEL_node(self, node):
        temp = None
        if not node:
            return node
        elif self.get_balance(node) < 0:
            temp = self.get_min_node(node)
        elif self.get_balance(node) > 0:
            temp = self.get_max_node(node)
        else:
            if node.key - node.left.key < node.right.key - node.key:
                temp = self.get_max_node(node)
            else:
                temp = self.get_min_node(node)

        return

    def Print(self, node):
        """Вивід дерева"""
        if not node:
            return

        print(node.key, end=" ")
        self.Print(node.left)
        self.Print(node.right)
        return

def main():
    Tree = AVL_Tree()
    root = None

    # root = Tree.insert(root, 9, "jhdkjaqsl")
    # root = Tree.insert(root, 5, "jhdksjasl")
    # root = Tree.insert(root, 10, "jhdkjafsl")
    # root = Tree.insert(root, 0, "jhadkjasl")
    # root = Tree.insert(root, 6, "jhdakjasl")
    # root = Tree.insert(root, 11, "jhdkfjasl")
    # root = Tree.insert(root, -1, "jhdkfjasl")
    # root = Tree.insert(root, 1, "jhdkfjasl")
    # root = Tree.insert(root, 2, "jhdkfjasl")
    root = Tree.insert(root, 10, "jhdkjaqsl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 6, "jhdksjasl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 16, "jhdkjafsl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 4, "jhadkjasl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 7, "jhdakjasl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 3, "jhdkfjasl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 12, "jhdkfjasl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 22, "jhdkfjasl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 14, "jhdkfjasl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 19, "jhdkjaqsl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 24, "jhdksjasl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 17, "jhdkjafsl")
    Tree.Print(root)
    print()
    root = Tree.insert(root, 21, "jhadkjasl")

    Tree.Print(root)

    # root = Tree.Delete(root, 10)
    root = Tree.delete(root, 10)
    print()
    Tree.Print(root)
    return

if __name__ == "__main__":
    main()
