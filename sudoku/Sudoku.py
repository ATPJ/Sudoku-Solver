from sudoku.util import FilterMode


class Sudoku:
    def __init__(self,
                 board: list[list[int]],
                 filter_mode: FilterMode) -> None:
        self.board = board
        self.traced = 0
        self.filter_mode: FilterMode = filter_mode

    def show_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print('- - - - - - - - - - -')
            for j in range(len(self.board)):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j], end=" ")

    def is_valid(self, pos: tuple[int, int], num: int) -> bool:
        r, c = pos

        # Checking the rows at r
        for j in range(len(self.board[0])):
            if self.board[r][j] == num:
                return False

        # Chccking the columns at c
        for i in range(len(self.board)):
            if self.board[i][c] == num:
                return False

        # check the box:
        box_x = r // 3
        box_y = c // 3
        for i in range(box_x * 3, box_x * 3 + 3):
            for j in range(box_y * 3, box_y * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty_cell(self) -> tuple[int, int] | None:
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    return (i, j)

    def __find_empty_cell_with_mre_startgey(self):
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))

        if len(empty_cells) <= 0:
            return None
        res = []
        for e in empty_cells:
            cost = 0
            x, y = e
            for i in range(9):
                if self.board[x][i] == 0 and i != y:
                    cost += 1
                if self.board[i][y] == 0 and i != x:
                    cost += 1

            res.append(((x, y), cost))

        res.sort(key=lambda k: k[1])
        return res[0][0]

    def solve(self):
        if self.filter_mode.value == FilterMode.nothing.value:
            empty_cell = self.find_empty_cell()
        if self.filter_mode.value == FilterMode.mrv.value:
            empty_cell = self.__find_empty_cell_with_mre_startgey()
        if empty_cell is None:
            return (self.board, True, self.traced)
        else:
            row, col = empty_cell

        for i in range(1, 10):
            if self.is_valid(empty_cell, i):
                self.board[row][col] = i

                _next_s = Sudoku(self.board, self.filter_mode)
                self.traced += 1
                res = _next_s.solve()
                self.traced += res[2]
                if res[1]:
                    self.board = res[0]
                    return (self.board, True, self.traced)

                self.board[row][col] = 0

        return (self.board, False, self.traced)
