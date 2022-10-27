import random
import networkx as nx
import matplotlib.pyplot as plt

class General:
    """Клас із загальними полями та методами"""

    def __init__(self):
        """Конструктор"""
        self.GRAPH = [
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]]
        self.EDGES = ["red", "blue", "yellow", "green", "silver", "gray", "maroon", "olive", "lime", "aqua",
                      "teal", "navy", "fuchsia", "purple", "indianred", "khaki", "salmon", "peachpuff", "lightyellow",
                      "chocolate", "firebrick", "azure", "coral", "orange", "tan"]
        self.COLORS = ["red", "blue", "yellow", "green"]
        self.POSITION = {1: (600, 550), 2: (346, 281), 3: (196, 94), 4: (608, 310), 5: (747, 314), 6: (348, 144), 7: (101, 302),
               8: (668, 387), 9: (175, 289),
               10: (442, 188), 11: (487, 307), 12: (800, 228), 13: (150, 215), 14: (486, 383), 15: (421, 421),
               16: (560, 210), 17: (276, 122), 18: (565, 104),
               19: (228, 234), 20: (665, 200), 21: (560, 430), 22: (285, 235), 23: (450, 250), 24: (237, 332),
               25: (490, 84)}
        self.Start_edge = self.Edge = 0
        self.Result = None

        # Для тестування
        self.Number_of_iterations = 0
        self.Number_of_conditions = 0
        self.Number_of_dead_ends = 0
        return

    def drow_graph(self, edges):
        """Малювання графу"""
        Graph = nx.Graph()
        plt.gca().invert_yaxis()
        Graph.add_nodes_from(self.POSITION.keys())
        for i in range(len(self.GRAPH)):
            for j in range(i):
                if self.GRAPH[i][j]:
                    Graph.add_edge(i + 1, j + 1)
        for n, p in self.POSITION.items():
            Graph.nodes[n]['pos'] = p
        nx.draw(Graph, node_color=edges, with_labels=True, pos=self.POSITION)
        plt.show()
        return

    def set_random_Start_edge(self):
        """Початкова вершина (початковий стан)"""
        self.Start_edge = self.Edge = random.randint(0, len(self.GRAPH) - 1)
        return self.Start_edge

    def set_Start_edge(self, edge):
        """Початкова вершина (початковий стан)"""
        self.Start_edge = self.Edge = edge
        return self.Start_edge

    def number_of_colors(self, edges):
        """Кількість кольорів"""
        colors = []
        for i in edges:
            if not i in colors:
                colors += [i]
        return len(colors)

class Algorithm_Hill(General):
    """Алгоритм сходження до вершини"""

    def __init__(self):
        """Конструктор"""
        super().__init__()
        random.shuffle(self.EDGES)
        return

    def check(self, index, edges, color):
        """Перевірка фарбування"""
        for i in range(len(self.GRAPH[index])):
            self.Number_of_iterations += 1
            if self.GRAPH[index][i] == 1:
                if color == edges[i]:
                    return False
        return True

    def Hill(self):
        """Сходження до вершини"""
        edges = self.EDGES.copy()
        flag = True
        flags = [True for i in range(len(edges))]
        while flag:
            self.Number_of_iterations += 1
            if flags[self.Edge]:
                self.Number_of_conditions += 1
                for color in self.COLORS:
                    self.Number_of_iterations += 1
                    if self.check(self.Edge, edges, color):
                        edges[self.Edge] = color
                        flags[self.Edge] = False
                        break
                if flags[self.Edge]:
                    flag = False
            else:
                temp = self.Edge
                for i in range(len(edges)):
                    self.Number_of_iterations += 1
                    if self.GRAPH[self.Edge][i] == 1:
                        if flags[i]:
                            self.Edge = i
                            break
                if temp == self.Edge:
                    flag = False
        return edges

    def side_movement(self, edges, edge):
        """Рух убік"""
        for i in range(100):
            self.Number_of_iterations += 1
            self.Number_of_conditions += 1
            colours = []
            for color in self.COLORS:
                self.Number_of_iterations += 1
                if self.check(edge, edges, color):
                    colours += [color]
            if len(colours) > 0:
                flag = True
                for i in colours:
                    self.Number_of_iterations += 1
                    temp = edges.copy()
                    temp[edge] = i
                    if self.number_of_colors(temp) < self.number_of_colors(edges):
                        edges[edge] = i
                        flag = False
                        break
                if flag:
                    colour = random.choice(colours)
                    edges[edge] = colour
            if self.number_of_colors(edges) <= 4:
                break
            Edges = []
            for i in range(len(edges)):
                self.Number_of_iterations += 1
                if self.GRAPH[edge][i] == 1:
                    Edges += [i]
            edge = random.choice(Edges)
        return edges

    def start(self):
        """Запуск алгоритму"""
        self.Result = self.EDGES.copy()
        for i in range(10):
            edges = self.Hill()
            if self.number_of_colors(edges) > 4:
                for j in range(5):
                    self.Number_of_dead_ends += 1
                    edges = self.side_movement(edges.copy(), self.Edge)
                    if self.number_of_colors(edges) < self.number_of_colors(self.Result):
                        self.Result = edges
                    if self.number_of_colors(edges) <= 4:
                        break
                if self.number_of_colors(edges) <= 4:
                    self.Result = edges
                    break
            else:
                break
            self.set_random_Start_edge()
        return self.Result

class Algorithm_Backtracking(General):
    """Алгоритм з пошуку поверненням (backtracking)"""

    def __init__(self):
        """Конструктор"""
        super().__init__()
        return

    def from_dict_to_list(self, result):
        """Конвертація із словника у список"""
        res = []
        for i in range(len(self.GRAPH)):
            if i in result:
                res += [result[i]]
            else:
                for color in self.EDGES:
                    if not color in res:
                        res += [color]
                        break
        return res

    def mrv(self, edges):
        """Визначення фарбування вузла"""
        numbers = {}
        for i in range(len(self.GRAPH)):
            self.Number_of_iterations += 1
            if not i in edges:
                numbers[i] = self.COLORS.copy()
                for j in range(len(self.GRAPH)):
                    self.Number_of_iterations += 1
                    if self.GRAPH[i][j]:
                        if j in edges:
                            if edges[j] in numbers[i]:
                                numbers[i].remove(edges[j])
        min = len(self.COLORS) + 1
        index = None
        for i in numbers:
            self.Number_of_iterations += 1
            if len(numbers[i]) < min:
                min = len(numbers[i])
                index = i
        if min == 0 or min == len(self.COLORS) + 1:
            return -1, []
        return index, numbers[index]

    def Backtracking(self, edge, edges, colors):
        """Пошук з поверненням"""
        for i in colors:
            self.Number_of_iterations += 1
            self.Number_of_conditions += 1
            if len(edges) == len(self.GRAPH):
                self.Result = edges
                break
            edges[edge] = i
            edge, colours = self.mrv(edges)
            if edge == -1:
                self.Number_of_dead_ends += 1
                if len(self.Result) < len(edges):
                    self.Result = edges
                break
            edges = self.Backtracking(edge, edges, colours)
        return edges

    def start(self):
        """Запуск алгоритму"""
        self.Result = {}
        result = self.Backtracking(self.Start_edge, {}, self.COLORS.copy())
        self.Result = self.from_dict_to_list(result)
        return self.Result
