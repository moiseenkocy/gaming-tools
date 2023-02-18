import pytest

from sudoku.helpers import CellIndex, get_cells_in_column


@pytest.mark.parametrize(
    "cell, expected_result",
    [
        (
            CellIndex(row=4, column=5),
            [
                CellIndex(row=0, column=5),
                CellIndex(row=1, column=5),
                CellIndex(row=2, column=5),
                CellIndex(row=3, column=5),
                CellIndex(row=4, column=5),
                CellIndex(row=5, column=5),
                CellIndex(row=6, column=5),
                CellIndex(row=7, column=5),
                CellIndex(row=8, column=5),
            ],
        ),
    ],
)
def test_get_cells_in_column(cell: CellIndex, expected_result: CellIndex) -> None:
    # Act
    result = get_cells_in_column(cell)

    # Assert
    assert result == expected_result
