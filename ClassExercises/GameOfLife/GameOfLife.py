class cell:

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state


class grid:

    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.grid = list()
        for i in range(self.rows):
            row_list = list()
            for j in range(self.cols):
                row_list.append('-')
            self.grid.append(row_list)

    def printGrid(self):
        for row in range(self.rows):
            print(self.grid[row])

    def next_move(self):
        pass

    def set_cell(self, x, y, state):
        if state == 0:
            self.grid[x][y] = '-'
        else:
            self.grid[x][y] = 'X'

    def play(self, ticks):
        pass


gofl = grid(20, 10)
gofl.set_cell(2, 8, 1)
gofl.set_cell(3, 4, 1)
gofl.set_cell(5, 9, 1)
gofl.set_cell(8, 1, 1)
gofl.set_cell(18, 4, 1)
gofl.printGrid()
