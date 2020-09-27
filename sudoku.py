import copy
from collections import Counter


class Solver:
    def __init__(self, field):
        self.field = field
        self.solution = False

    def solve(self, field, pos):
        if self.solution is False:
            if pos:
                if field[pos[0]][pos[1]] < 9:
                    field[pos[0]][pos[1]] += 1
                    if self.validate(field):
                        if not self.solve(field, self.find_empty(field)):
                            return self.solve(field, pos)
                    else:
                        return self.solve(field, pos)
                else:
                    field[pos[0]][pos[1]] = 0
                    return False
            else:
                if self.validate(field) and self.find_empty(field) is False:
                    self.solution = field
                    print(self)
                    return True
                else:
                    return False

    def find_empty(self, field):
        for x in range(len(field)):
            for y in range(len(field)):
                num = field[x][y]
                if num == 0:
                    return (x, y)
        return False

    def validate_list(self, values):
        c = Counter(values)
        most_common = c.most_common(2)
        for i in most_common:
            if i[0] != 0 and i[1] > 1:
                return False
        return True

    def validate(self, field):
        field = [copy.copy(i) for i in field]
        # row
        for row in field:
            if not self.validate_list(row):
                return False
        # column
        for i in range(len(field)):
            column = [column[i] for column in field]
            if not self.validate_list(column):
                return False
        # block
        blocks = []
        while field:
            block = []
            for row in field[:3]:
                for i in range(3):
                    block.append(row.pop())
            blocks.append(block)
            if field[0] == []:
                for i in range(3):
                    field.pop(0)
        for block in blocks:
            if not self.validate_list(block):
                return False
        return True

    def empty_if_zero(self, i):
        if i == 0:
            return "  "
        else:
            return f"{i} "

    def __str__(self):
        if self.solution:
            field = copy.deepcopy(self.solution)
        else:
            field = copy.deepcopy(self.field)

        print_string = ""
        row_counter = 0
        for i in field:
            i.insert(3, "|")
            i.insert(7, "|")
            print_string += "".join([self.empty_if_zero(j) for j in i])
            print_string += "\n"
            if row_counter == 2 or row_counter == 5:
                print_string += "---------------------\n"
            row_counter += 1
        return print_string


if __name__ == "__main__":
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
    field = [
    ]
    solver = Solver(field)
    pos = solver.find_empty(field)
    solver.solve(field, pos)
