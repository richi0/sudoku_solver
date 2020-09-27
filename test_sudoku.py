import copy

import numpy as np

from sudoku import Solver



field = [
    [3, 2, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 4, 0, 8, 3, 0, 0, 0],
    [7, 5, 0, 0, 9, 0, 0, 0, 0],
    [5, 3, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 2, 7],
    [0, 0, 0, 0, 1, 0, 0, 3, 6],
    [0, 0, 0, 9, 6, 0, 2, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 8, 1]
]

field2 = [
    [5, 3, 0, 4, 0, 0, 0, 0, 0],
    [9, 1, 0, 0, 2, 0, 0, 3, 5],
    [0, 0, 2, 0, 3, 0, 1, 4, 0],
    [2, 0, 9, 0, 8, 0, 4, 0, 3],
    [0, 5, 0, 2, 6, 4, 0, 0, 0],
    [0, 0, 0, 9, 7, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 7, 0, 1, 4],
    [7, 4, 0, 0, 1, 0, 0, 9, 8],
    [0, 2, 6, 0, 4, 0, 3, 0, 0]
]

solver = Solver(field)


def test_list_validate():
    row = np.array([3, 2, 0, 0, 0, 0, 0, 6, 0])
    assert solver.validate_list(row) == True
    row = np.array([3, 2, 0, 0, 0, 3, 0, 6, 0])
    assert solver.validate_list(row) == False


def test_field_validate():
    assert solver.validate(solver.field) == True
    test_field = copy.deepcopy(solver.field)
    test_field[0][8] = 1
    # validate row
    assert solver.validate(test_field) == False
    test_field = copy.deepcopy(solver.field)
    test_field[0][8] = 2
    # validate column
    assert solver.validate(test_field) == False
    test_field = copy.deepcopy(solver.field)
    test_field[1][6] = 6
    # validate block
    assert solver.validate(test_field) == False


def test_find_empty():
    assert solver.find_empty(solver.field) == (0, 2)
    test_field = [1 for x in range(9)]
    test_field = np.array([np.array(test_field) for x in range(9)])
    assert solver.find_empty(test_field) == False


def test_solve():
    solution1 = np.array([
        np.array([3, 2, 9, 1, 4, 7, 5, 6, 8]),
        np.array([1, 6, 4, 5, 8, 3, 7, 9, 2]),
        np.array([7, 5, 8, 2, 9, 6, 3, 1, 4]),
        np.array([5, 3, 2, 8, 7, 1, 6, 4, 9]),
        np.array([4, 7, 1, 6, 2, 9, 8, 5, 3]),
        np.array([9, 8, 6, 4, 3, 5, 1, 2, 7]),
        np.array([2, 4, 5, 7, 1, 8, 9, 3, 6]),
        np.array([8, 1, 3, 9, 6, 4, 2, 7, 5]),
        np.array([6, 9, 7, 3, 5, 2, 4, 8, 1])
    ])
    pos = solver.find_empty(solver.field)
    solver.solve(solver.field, pos)
    comparison = solver.solution == solution1
    print(solver.solution)
    print(solution1)
    assert comparison.all() == True

    solution2 = np.array([
        np.array([5, 3, 8, 4, 9, 1, 7, 2, 6]),
        np.array([9, 1, 4, 7, 2, 6, 8, 3, 5]),
        np.array([6, 7, 2, 5, 3, 8, 1, 4, 9]),
        np.array([2, 6, 9, 1, 8, 5, 4, 7, 3]),
        np.array([3, 5, 7, 2, 6, 4, 9, 8, 1]),
        np.array([4, 8, 1, 9, 7, 3, 5, 6, 2]),
        np.array([8, 9, 3, 6, 5, 7, 2, 1, 4]),
        np.array([7, 4, 5, 3, 1, 2, 6, 9, 8]),
        np.array([1, 2, 6, 8, 4, 9, 3, 5, 7])
    ])
    solver2 = Solver(field2)
    pos = solver2.find_empty(solver2.field)
    solver2.solve(solver2.field, pos)
    comparison = solver2.solution == solution2
    assert comparison.all() == True