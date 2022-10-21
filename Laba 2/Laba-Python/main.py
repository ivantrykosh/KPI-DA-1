from random import randint
from random import choice
from random import shuffle
import networkx as nx
import matplotlib.pyplot as plt
import Functional

def edge(graph):
    """Початкова вершина (початковий стан)"""
    return randint(0, len(graph) - 1)

def same_color(graph, edges):
    """Функція для визначення кількості конфліктів"""
    number = 0
    for i in range(len(edges)):
        for j in range(i):
            if graph[i][j]:
                if edges[i] == edges[j]:
                    number += 1
    return number

def hill(graph, edges, edge, colors):
    """Сходження на вершину"""
    flag = True
    while flag:
        number = same_color(graph, edges)
        temp = []
        for i in range(len(edges)):
            index = None
            colour = None
            number_of_conflicts = number
            if graph[edge][i]:
                for color in colors:
                    copy_edges = edges.copy()
                    copy_edges[i] = color
                    temp_number_conflicts = same_color(graph, copy_edges)
                    if temp_number_conflicts < number and temp_number_conflicts < number_of_conflicts:
                        colour = color
                        index = i
                        number_of_conflicts = temp_number_conflicts
            if index != None:
                temp += [[number_of_conflicts, index, colour]]
        if len(temp) == 0:
            flag = False
        else:
            minimum = float("inf")
            index = None
            color = None
            for i in temp:
                if minimum > i[0]:
                    minimum = i[0]
                    index = i[1]
                    color = i[2]
            edges[index] = color
            edge = index
            # print(f"{index}:{color}")

    if same_color(graph, edges) > 0:
        for i in range(100):
            number = same_color(graph, edges)
            temp = []
            for i in range(len(edges)):
                index = None
                colour = None
                number_of_conflicts = number
                if graph[edge][i]:
                    for color in colors:
                        if color != edges[i]:
                            copy_edges = edges.copy()
                            copy_edges[i] = color
                            temp_number_conflicts = same_color(graph, copy_edges)
                            if temp_number_conflicts <= number:
                                temp += [[temp_number_conflicts, i, color]]
            if len(temp) != 0:
                # print(temp)
                minimum = float("inf")
                index = None
                color = None
                for i in temp:
                    if minimum > i[0]:
                        minimum = i[0]
                        index = i[1]
                        color = i[2]
                edges[index] = color
                edge = index

                items = []
                for i in temp:
                    if minimum == i[0]:
                        items += [i]
                randitem = choice(items)
                edges[randitem[1]] = randitem[2]
                edge = randitem[1]
                # print(f"{index}:{color}")
    return edges

def check(graph_line, edges, color):
    """Функція для перевірки фарбування"""
    for i in range(len(graph_line)):
        if graph_line[i] == 1:
            if color == edges[i]:
                return False
    return True

def Hill(graph, edges, edge, colors):
    """Сходження до вершини і рух убік"""
    flag = True
    flags = [True for i in range(len(edges))]
    while flag:
        if flags[edge]:
            for color in colors:
                if check(graph[edge], edges, color):
                    edges[edge] = color
                    flags[edge] = False
                    break
            if flags[edge]:
                flag = False
        else:
            temp = edge
            for i in range(len(edges)):
                if graph[edge][i] == 1:
                    if flags[i]:
                        edge = i
                        break
            if temp == edge:
                flag = False

    # if True in flags:
    #     for i in range(100):
    #         colours = []
    #         for color in colors:
    #             if check(graph[edge], edges, color):
    #                 colours += [color]
    #         if len(colours) > 0:
    #             colour = choice(colours)
    #             edges[edge] = colour
    #
    #         Edges = []
    #         for i in range(len(edges)):
    #             if graph[edge][i] == 1:
    #                 Edges += [i]
    #         edge = choice(Edges)
    return edges, edge

def side_movement(graph, edges, Edge, colors):
    """Рух убік"""
    for i in range(100):
        colours = []
        for color in colors:
            if check(graph[Edge], edges, color):
                colours += [color]
        if len(colours) > 0:
            colour = choice(colours)
            edges[Edge] = colour

        Edges = []
        for i in range(len(edges)):
            if graph[Edge][i] == 1:
                Edges += [i]
        Edge = choice(Edges)
    return edges

def number_of_colors(edges):
    """Кількість кольорів"""
    colors = []
    for i in edges:
        if not i in colors:
            colors += [i]
    return len(colors)

def graph(graph, edges):
    """Малювання графу"""
    pos = {1: (600, 550), 2: (346, 281), 3: (196, 94), 4: (608, 310), 5: (747, 314), 6: (348, 144), 7: (101, 302), 8: (668, 387), 9: (175, 289),
           10: (442, 188), 11: (487, 307), 12: (800, 228), 13: (150, 215), 14: (486, 383), 15: (421, 421), 16: (560, 210), 17: (276, 122), 18: (565, 104),
           19: (228, 234), 20: (665, 200), 21: (560, 430), 22: (285, 235), 23: (450, 250), 24: (237, 332), 25: (490, 84)}
    Graph = nx.Graph()
    plt.gca().invert_yaxis()
    # plt.gca().invert_xaxis()
    # for i in range(len(edges)):
    #     Graph.add_node(i + 1)
    # for i in range(len(edges)):
    #     Graph.nodes[i]["pos"] = pos[i]
    Graph.add_nodes_from(pos.keys())
    for i in range(len(edges)):
        for j in range(i):
            if graph[i][j]:
                Graph.add_edge(i + 1, j + 1)
    for n, p in pos.items():
        Graph.nodes[n]['pos'] = p
    nx.draw(Graph, node_color=edges, with_labels=True, pos=pos)
    plt.show()
    return

# def mrv(graph, edge, edges, colors):
#     """Визначення фарбування вузла"""
#     numbers = {}
#     for i in range(len(graph)):
#         if graph[edge][i]:
#             if not i in edges:
#                 numbers[i] = colors.copy()
#                 for j in range(len(graph)):
#                     if graph[i][j]:
#                         if j in edges:
#                             if edges[j] in numbers[i]:
#                                 numbers[i].remove(edges[j])
#     min = len(colors) + 1
#     index = None
#     for i in numbers:
#         if len(numbers[i]) < min:
#             min = len(numbers[i])
#             index = i
#     if min == 0:
#         return -1, None
#     return i, numbers[i]
def mrv(graph, edges, colors):
    """Визначення фарбування вузла"""
    numbers = {}
    for i in range(len(graph)):
        if not i in edges:
            numbers[i] = colors.copy()
            for j in range(len(graph)):
                if graph[i][j]:
                    if j in edges:
                        if edges[j] in numbers[i]:
                            numbers[i].remove(edges[j])
    min = len(colors) + 1
    index = None
    for i in numbers:
        if len(numbers[i]) < min:
            min = len(numbers[i])
            index = i
    if min == 0:
        return -1, None
    if min == 5:
        return -1, []
    return index, numbers[index]

def move(graph, edge, edges, colors, const_colors):
    for i in colors:
        if len(edges) == len(graph):
            break
        edges[edge] = i
        edge, colours = mrv(graph, edges, const_colors)
        if edge == -1:
            break
        edges = move(graph, edge, edges, colours, const_colors)
    return edges

def backtracking(graph, edge, colors):
    """Пошук з поверненням""" # popitem and by index
    # tree = Tree.Tree((edge, None))
    edges = {}
    result = {}
    # sons = [tree.left1, tree.left2, tree.right1, tree.right2]
    # flag = True
    # if len(colors):
    #     for i in range(len(colors)):
    #         sons[i] = Tree.Tree((edge, colors[i]))
    # else:
    #     return
    # while flag:
    #     for i in colors:
    #         edges[edge] = i
    #         edge, colours = mrv(graph, edge, edges, colors)
    result = move(graph, edge, edges, colors, colors)
    res = []
    # for i in range(len(result)):
    #     res += [result[i]]
    for i in range(len(graph)):
        if i in result:
            res += [result[i]]
        else:
            res += ["white"]
    return res

def Main():
    GRAPH = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
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
    COLORS = ["red", "blue", "yellow", "green"]
    res = backtracking(GRAPH, edge(GRAPH), COLORS)
    print(res)
    graph(GRAPH, res)
    INDEX = None
    EDGES = ["red", "blue", "yellow", "green", "silver", "gray", "maroon", "olive", "lime", "aqua",
             "teal", "navy", "fuchsia", "purple", "indianred", "khaki", "salmon", "peachpuff", "lightyellow", "chocolate",
             "firebrick", "azure", "coral", "orange", "tan"]
    result = EDGES.copy()
    shuffle(EDGES)
    graph(GRAPH, EDGES)
    for i in range(10):
        # EDGES = ["red" for i in range(len(GRAPH))]
        index = edge(GRAPH)
        # index = 5
        print(f"The first edge = {index}")
        edges, Edge = Hill(GRAPH, EDGES.copy(), index, COLORS)
        # print(f"The number of conflicts = {same_color(GRAPH, EDGES)}")
        if number_of_colors(edges) > 4:
            for j in range(5):
                # edges = hill(GRAPH, EDGES, index, COLORS)
                edges = side_movement(GRAPH, edges.copy(), Edge, COLORS)
                # for i in range(len(edges)):
                #     print(f"{i+1}=\"{edges[i]}\"")
                # print(f"The number of conflicts = {same_color(GRAPH, edges)}")
                # if same_color(GRAPH, edges) < same_color(GRAPH, result):
                #     result = edges
                #     INDEX = index
                # if same_color(GRAPH, edges) == 0:
                #     result = edges
                #     break
                if number_of_colors(edges) < number_of_colors(result):
                    result = edges
                    INDEX = index
                if number_of_colors(edges) <= 4:
                    print(f"Made {j+1} iterations")
                    break
            if number_of_colors(edges) <= 4:
                result = edges
                INDEX = index
                break
        else:
            break
    # print(f"\n\nResult (first edge:{INDEX}, conflicts:{same_color(GRAPH, result)}):")
    print(f"\n\nResult (first edge:{INDEX}, number of colors:{number_of_colors(result)}):")
    for i in range(len(result)):
        print(f"{i+1}=\"{result[i]}\"", end="; ")
    graph(GRAPH, result)
    return

def main():
    test = None
    if int(input("Choose algorithm (0 - Hill, 1 - Backtracking): ")) == 0:
        test = Functional.Algorithm_Hill()
        test.drow_graph(test.EDGES)
        test.set_random_Start_edge()
        test.start()
        test.drow_graph(test.Result)
    else:
        test = Functional.Algorithm_Backtracking()
        test.set_random_Start_edge()
        test.start()
        test.drow_graph(test.Result)
    return

if __name__ == "__main__":
    main()
