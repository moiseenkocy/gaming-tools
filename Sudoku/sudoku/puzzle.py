from typing import List

from sudoku.cell import SudokuCell


class SudokuPuzzle:
    def __init__(self, puzzle: List[List[int]]) -> None:
        self.data = [
            [SudokuCell(puzzle[row][column]) for column in range(9)] for row in range(9)
        ]

    def __getitem__(self, row: int) -> List[int]:
        return self.data[row]
