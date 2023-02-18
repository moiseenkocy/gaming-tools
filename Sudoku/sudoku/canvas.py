from typing import Set, Tuple


class SudokuCanvas:
    def __init__(self) -> None:
        self.canvas = [[" " for column in range(49)] for row in range(37)]

        self._add_horizontal_lines()
        self._add_vertical_lines()
        self._add_crosses()
        self._add_corners()
        self._add_t_junctions()

    def _add_horizontal_lines(self) -> None:
        for h_line in range(4):
            for column in range(49):
                self.canvas[h_line * 12][column] = "─"

    def _add_vertical_lines(self) -> None:
        for v_line in range(4):
            for row in range(37):
                self.canvas[row][v_line * 16] = "│"

    def _add_crosses(self) -> None:
        for h_line in range(1, 3):
            for v_line in range(1, 3):
                self.canvas[h_line * 12][v_line * 16] = "┼"

    def _add_corners(self) -> None:
        self.canvas[0][0], self.canvas[0][48] = "┌", "┐"
        self.canvas[36][0], self.canvas[36][48] = "└", "┘"

    def _add_t_junctions(self) -> None:
        for v_line in range(1, 3):
            self.canvas[0][v_line * 16] = "┬"

        for h_line in range(1, 3):
            self.canvas[h_line * 12][0] = "├"
            self.canvas[h_line * 12][48] = "┤"

        for v_line in range(1, 3):
            self.canvas[36][v_line * 16] = "┴"

    def _get_cell_index(self, row: int, column: int) -> Tuple[int, int]:
        return row * 4 + 1, column // 3 * 16 + column % 3 * 5 + 2

    def _clean_cell(self, row: int, column: int) -> None:
        cell_row, cell_column = self._get_cell_index(row, column)
        for i in range(cell_row, cell_row + 3):
            for j in range(cell_column - 1, cell_column + 3 + 1):
                self.canvas[i][j] = " "

    def clean(self) -> None:
        for row in range(9):
            for column in range(9):
                self._clean_cell(row, column)

    def render(self) -> str:
        return "\n".join(["".join(self.canvas[row]) for row in range(37)])

    def write_solved(self, row: int, column: int, value: int) -> None:
        self._clean_cell(row, column)

        i, j = self._get_cell_index(row, column)

        self.canvas[i][j], self.canvas[i][j + 2] = "┌", "┐"
        self.canvas[i][j + 1], self.canvas[i + 2][j + 1] = "─", "─"
        self.canvas[i + 1][j], self.canvas[i + 1][j + 2] = "│", "│"
        self.canvas[i + 2][j], self.canvas[i + 2][j + 2] = "└", "┘"

        self.canvas[i + 1][j + 1] = str(value)

    def write_unsolved(self, row: int, column: int, values: Set[int]) -> None:
        self._clean_cell(row, column)

        i, j = self._get_cell_index(row, column)

        for v in range(1, 10):
            i_offset, j_offset = divmod(v - 1, 3)
            self.canvas[i + i_offset][j + j_offset] = str(v) if v in values else "."
