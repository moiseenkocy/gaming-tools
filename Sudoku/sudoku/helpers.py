from dataclasses import dataclass
from typing import List


@dataclass
class CellIndex:
    """Sudoku cell coordinates."""

    row: int
    column: int


def get_box_by_cell(cell: CellIndex) -> CellIndex:
    """Calculate upper-left point of given box."""
    return CellIndex(row=cell.row // 3 * 3, column=cell.column // 3 * 3)


def get_cells_in_row(cell: CellIndex) -> List[CellIndex]:
    """Calculate all cell coordinates for given row."""
    return [CellIndex(row=cell.row, column=column) for column in range(9)]


def get_cells_in_column(cell: CellIndex) -> List[CellIndex]:
    """Calculate all cell coordinates for given column."""
    return [CellIndex(row=row, column=cell.column) for row in range(9)]


def get_cells_in_box(cell: CellIndex) -> List[CellIndex]:
    """Calculate all cell coordinates for given box."""
    box_index = get_box_by_cell(cell)
    return [
        CellIndex(row=row, column=column)
        for row in range(box_index.row, box_index.row + 3)
        for column in range(box_index.column, box_index.column + 3)
    ]


def get_neighbours_in_row(cell: CellIndex) -> List[CellIndex]:
    """Calculate all neighbours in given row."""
    return list(filter(cell.__ne__, get_cells_in_row(cell)))


def get_neighbours_in_column(cell: CellIndex) -> List[CellIndex]:
    """Calculate all neighbours in given column."""
    return list(filter(cell.__ne__, get_cells_in_column(cell)))


def get_neighbours_in_box(cell: CellIndex) -> List[CellIndex]:
    """Calculate all neighbours in given box."""
    return list(filter(cell.__ne__, get_cells_in_box(cell)))
