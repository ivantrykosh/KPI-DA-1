import Functional

def main():
    if int(input("Choose algorithm (0 - Hill, 1 - Backtracking): ")) == 0:
        test = Functional.Algorithm_Hill()
        test.drow_graph(test.EDGES)
        test.set_random_Start_edge()
        # test.set_Start_edge(20)
        print(f"Start Edge: {test.Start_edge}")
        test.start()
        print(f"\tThe number of iterations: {test.Number_of_iterations}")
        print(f"\tThe number of dead ends: {test.Number_of_dead_ends}")
        print(f"\tThe number of conditions: {test.Number_of_conditions}")
        print(f"Result: {test.Result}")
        test.drow_graph(test.Result)
    else:
        test = Functional.Algorithm_Backtracking()
        test.set_random_Start_edge()
        # test.set_Start_edge(20)
        print(f"Start Edge: {test.Start_edge}")
        test.start()
        print(f"\tThe number of iterations: {test.Number_of_iterations}")
        print(f"\tThe number of dead ends: {test.Number_of_dead_ends}")
        print(f"\tThe number of conditions: {test.Number_of_conditions}")
        print(f"Result: {test.Result}")
        test.drow_graph(test.Result)
    return

if __name__ == "__main__":
    main()
