# Sudoku solver

I used this script to try pytest and cProfile

## Optimising the script

Changes between versions:
- Removed deepcopy from solve methode
- Exit afther first solution is found.
- Replaced deepcopy with copy.copy inside validate methode.

Running time of the script in cProfile

|          | V 1 | V 2 | V 3 | V 4 | V 5 |
|----------|-----|-----|-----|-----|-----|
| Time (s) | 132 |  53 | 22  | 7   | 6   |

Outside of cProfile the script runs much faster. It depends on the sudoku. The first sudoku in the test_sudoku file runs in 3 seconds. The second one in 0.2 seconds.