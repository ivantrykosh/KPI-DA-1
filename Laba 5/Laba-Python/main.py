import random

class Stuff:
    """Предмет"""
    def __init__(self):
        """Конструктор"""
        self.price = random.randint(2, 30)
        self.weight = random.randint(1, 20)
        return

    def get_stuff(self):
        """Отримання предмету як рядка"""
        return "price = " + str(self.price) + ", weight = " + str(self.weight) + ";  "

class Backpack:
    """Рюкзак"""
    def __init__(self):
        """Конструктор"""
        self.capacity = 500
        self.number = 100
        self.result = []
        return

class Algorithm:
    """Генетичний алгоритм"""
    def __init__(self):
        """Конструктор"""
        self.backpack = Backpack()
        self.stuffs = [Stuff() for i in range(self.backpack.number)]
        self.population = []
        self.set_start_population()
        self.backpack.result = self.best_chromosome()
        self.numb = 0
        return

    def set_start_population(self):
        """Встановлення початкової популяції"""
        for i in range(self.backpack.number):
            self.population += [[0 for j in range(self.backpack.number)]]
            self.population[i][i] = 1
        return

    def chromosome_price(self, chromosome):
        """Ціна хромосоми (особи)"""
        price = 0
        for i in range(len(chromosome)):
            price += chromosome[i] * self.stuffs[i].price
        return price

    def chromosome_weight(self, chromosome):
        """Вага хромосоми (особи)"""
        weight = 0
        for i in range(len(chromosome)):
            weight += chromosome[i] * self.stuffs[i].weight
        return weight

    def best_chromosome(self):
        """Найкраща хромосома (особа) в популяції"""
        best = self.population[0]
        index = 0
        for i in range(1, len(self.population)):
            if self.chromosome_price(best) < self.chromosome_price(self.population[i]):
                best = self.population[i]
                index = i
        return index

    def worst_chromosome(self):
        """Найгірша хромосома (особа) в популяції"""
        worst = self.population[0]
        index = 0
        for i in range(1, len(self.population)):
            if self.chromosome_price(worst) > self.chromosome_price(self.population[i]):
                worst = self.population[i]
                index = i
        return index

    def choose_parents(self):
        """Вибір батьків"""
        index = self.best_chromosome()
        temp = self.population.copy()
        parent1 = temp.pop(index)
        parent2 = random.choice(temp)
        return parent1, parent2

    def crossing_1(self, parent1, parent2):
        """Одноточокове схрещування хромосом"""
        l = random.randint(0, len(parent1) - 1)
        result = parent1[:l] + parent2[l:]
        if self.chromosome_weight(result) > self.backpack.capacity:
            result = None
        return result

    def crossing_2(self, parent1, parent2):
        """Двоточкове схрещування хромосом"""
        l1 = random.randint(0, len(parent1) - 1)
        l2 = random.randint(0, len(parent1) - 1)
        result = []
        if l1 < l2:
            result = parent1[:l1] + parent2[l1:l2] + parent1[l2:]
        else:
            result = parent1[:l2] + parent2[l2:l1] + parent1[l1:]
        if self.chromosome_weight(result) > self.backpack.capacity:
            result = None
        return result

    def crossing_3(self, parent1, parent2):
        """Рівномірне схрещування хромосом"""
        result = []
        for i in range(len(parent1)):
            choice = random.randint(0, 1)
            if choice:
                result += [parent1[i]]
            else:
                result += [parent2[i]]
        if self.chromosome_weight(result) > self.backpack.capacity:
            result = None
        return result

    def mutation_1(self, chromosome):
        """Ймовірнісна мутація хромосоми"""
        result = chromosome.copy()
        numb = random.randint(1, 10)
        if numb == 1:
            index = random.choice(range(len(result)))
            result[index] = 1 - result[index]
            self.numb += 1
        if self.chromosome_weight(result) > self.backpack.capacity:
            result = chromosome.copy()
        return result

    def mutation_2(self, chromosome):
        """Мутація хромосоми з переміщенням генів"""
        result = chromosome.copy()
        zeroes = []
        ones = []
        for i in range(len(result)):
            if result[i]:
                ones += [i]
            else:
                zeroes += [i]
        if len(zeroes) > 0 and len(ones) > 0:
            gene1 = random.choice(zeroes)
            gene2 = random.choice(ones)
            result[gene1], result[gene2] = result[gene2], result[gene1]
            if self.chromosome_weight(result) > self.backpack.capacity:
                result = chromosome.copy()
        return result

    def get_min_stuff(self, chromosome):
        """Отримання предмету з мінімальною вагою"""
        index = 0
        while chromosome[index]:
            index += 1
        min_stuff = self.stuffs[index]
        for i in range(index + 1, len(self.stuffs)):
            if not chromosome[i]:
                if min_stuff.weight > self.stuffs[i].weight:
                    min_stuff = self.stuffs[i]
                    index = i
        return index

    def improvement_1(self, chromosome):
        """Локальне покращення (додавання у рюкзак предмету з мінімальною вагою)"""
        index = self.get_min_stuff(chromosome)
        result = chromosome.copy()
        result[index] = 1
        if self.chromosome_weight(result) > self.backpack.capacity:
            result = chromosome.copy()
        return result

    def get_max_stuff_price(self, stuffs_indexes):
        """Отримати предмет з максимальною ціною"""
        max_stuff_index = 0
        if len(stuffs_indexes):
            max_stuff_index = stuffs_indexes[0]
            max_stuff_price = self.stuffs[max_stuff_index].price
            for i in stuffs_indexes:
                if self.stuffs[i].price > max_stuff_price:
                    max_stuff_price = self.stuffs[i].price
                    max_stuff_index = i
                elif self.stuffs[i].price == max_stuff_price and self.stuffs[i].weight < self.stuffs[
                    max_stuff_index].weight:
                    max_stuff_price = self.stuffs[i].price
                    max_stuff_index = i
        return max_stuff_index

    def improvement_2(self, chromosome):
        """Локальне покращення (додавання у рюкзак предмета з допустимою вагою і найбільшою ціною)"""
        result = chromosome.copy()
        weight = self.chromosome_weight(result)

        stuffs_indexes = []
        for i in range(len(result)):
            if not result[i]:
                if self.backpack.capacity >= weight + self.stuffs[i].weight:
                    stuffs_indexes += [i]
        if len(stuffs_indexes):
            max_stuff_index = self.get_max_stuff_price(stuffs_indexes)
            result[max_stuff_index] = 1
        return result

    def start(self):
        """Запуск алгоритму"""
        for i in range(500):
            parent1, parent2 = self.choose_parents()
            temp = self.crossing_1(parent1, parent2)
            if temp:
                temp = self.mutation_1(temp)
                temp = self.improvement_2(temp)
                self.population += [temp]
                self.population.pop(self.worst_chromosome())
                self.backpack.result = self.population[self.best_chromosome()]
                # if i % 20 == 19:
                #     print(f"Iteration:{i + 1}, value:{self.chromosome_price(self.backpack.result)}")

                # print("\n\nBest", i)
                # print("The weight of stuffs = ", self.chromosome_weight(self.backpack.result), "\nThe price of stuffs = ", self.chromosome_price(self.backpack.result))
                # numb = 0
                # for j in temp:
                #     if j:
                #         numb += 1
                # print("The number of stuffs:", numb)

                # print("\n\nResult:", i)
                # for j in range(len(temp)):
                #     if temp[j]:
                #         print(self.stuffs[j].get_stuff(), end="")
                # print("\nThe weight of stuffs = ", self.chromosome_weight(temp), "\nThe price of stuffs = ", self.chromosome_price(temp))
                # numb = 0
                # for j in temp:
                #     if j:
                #         numb += 1
                # print("The number of stuffs:", numb)
        return self.backpack.result

def main():
    algorithm = Algorithm()

    with open("stuffs.txt", "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i][:-1]
            if len(lines[i]) > 0:
                pos = 0
                for j in range(len(lines[i])):
                    if lines[i][j] == " ":
                        pos = j
                algorithm.stuffs[i].price, algorithm.stuffs[i].weight = int(lines[i][:pos]), int(lines[i][pos + 1:])


    # with open("stuffs.txt", "w") as file:
    #     for i in algorithm.stuffs:
    #         line = str(i.price) + " " + str(i.weight) + "\n"
    #         file.write(line)

    result = algorithm.start()

    print("\n\nStuffs:")
    for i in range(len(algorithm.stuffs)):
        print(algorithm.stuffs[i].get_stuff(), end="")
        if i % 5 == 4:
            print()
    print("\nResult:")
    numb = 0
    for i in range(len(result)):
        if result[i]:
            print(algorithm.stuffs[i].get_stuff(), end="")
            if numb % 5 == 4:
                print()
            numb += 1
    print("\nThe weight of stuffs = ", algorithm.chromosome_weight(result), "\nThe price of stuffs = ", algorithm.chromosome_price(result))
    numb = 0
    for j in result:
        if j:
            numb += 1
    print("The number of stuffs:", numb)
    return

if __name__ == "__main__":
    main()
