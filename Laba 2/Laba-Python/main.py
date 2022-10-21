import Functional

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
