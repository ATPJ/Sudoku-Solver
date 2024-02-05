from typer import Typer

from sudoku.Sudoku import Sudoku
from sudoku.util import FilterMode


app = Typer()


@app.command()
def main(mode: FilterMode):
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("-----------------------------------\nStarting State:\n")
    match mode:
        case mode.nothing:
            su = Sudoku(board, FilterMode.nothing)
        case mode.mrv:
            su = Sudoku(board, FilterMode.mrv)
    su.show_board()
    print("\n-----------------------------------\nSolved:\n")
    su.solve()
    su.show_board()
    print(f"\n{su.traced}")


if __name__ == "__main__":
    app()
