import pytest

from sudoku.helpers import CellIndex, get_cells_in_row


@pytest.mark.parametrize(
    "cell, expected_result",
    [
        (
            CellIndex(row=4, column=5),
            [
                CellIndex(row=4, column=0),
                CellIndex(row=4, column=1),
                CellIndex(row=4, column=2),
                CellIndex(row=4, column=3),
                CellIndex(row=4, column=4),
                CellIndex(row=4, column=5),
                CellIndex(row=4, column=6),
                CellIndex(row=4, column=7),
                CellIndex(row=4, column=8),
            ],
        ),
    ],
)
def test_get_cells_in_row(cell: CellIndex, expected_result: CellIndex) -> None:
    # Act
    result = get_cells_in_row(cell)

    # Assert
    assert result == expected_result
