from typing import List

from sudoku.canvas import SudokuCanvas
from sudoku.helpers import CellIndex, get_all_neighbours
from sudoku.puzzle import SudokuPuzzle


class SudokuSolver:
    def __init__(self, puzzle: List[List[int]]) -> None:
        self.puzzle = SudokuPuzzle(puzzle)

        self.strategies = [
            self.find_solved_cell,
            self.hidden_singles,
            self.naked_pairs,
            self.naked_triples,
        ]

    def solve(self) -> None:
        while True:
            for strategy in self.strategies:
                if strategy():
                    break
            else:
                break

    # Strategies
    def find_solved_cell(self) -> bool:
        for row in range(9):
            for column in range(9):
                cell = self.puzzle[row][column]
                if not cell.is_ready():
                    continue
                cell.solve()
                for ni in get_all_neighbours(CellIndex(row=row, column=column)):
                    self.puzzle[ni.row][ni.column].discard(cell.value)
                return True
        return False

    def hidden_singles(self) -> bool:
        return False

    def naked_pairs(self) -> bool:
        return False

    def naked_triples(self) -> bool:
        return False

    # Visualization
    def render(self) -> None: # pragma: no cover
        canvas = SudokuCanvas()
        for row in range(9):
            for column in range(9):
                cell = self.puzzle[row][column]
                if cell.solved:
                    canvas.write_solved(row, column, cell.value)
                else:
                    canvas.write_unsolved(row, column, cell.candidates)
        print(canvas.render())