import cProfile

from sudoku import Solver

with cProfile.Profile() as pr:
    field = [
        [3,2,0,0,0,0,0,6,0],
        [0,0,4,0,8,3,0,0,0],
        [7,5,0,0,9,0,0,0,0],
        [5,3,0,0,0,1,0,0,0],
        [0,0,1,0,0,0,8,0,0],
        [0,0,0,4,0,0,0,2,7],
        [0,0,0,0,1,0,0,3,6],
        [0,0,0,9,6,0,2,0,0],
        [0,9,0,0,0,0,0,8,1]
    ]
    solver = Solver(field)
    pos = solver.find_empty(field)
    solver.solve(field, pos)

pr.print_stats()