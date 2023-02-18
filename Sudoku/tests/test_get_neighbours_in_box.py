import pytest

from sudoku.helpers import CellIndex, get_neighbours_in_box


@pytest.mark.parametrize(
    "cell, expected_result",
    [
        (
            CellIndex(row=5, column=7),
            [
                CellIndex(row=3, column=6),
                CellIndex(row=3, column=7),
                CellIndex(row=3, column=8),
                CellIndex(row=4, column=6),
                CellIndex(row=4, column=7),
                CellIndex(row=4, column=8),
                CellIndex(row=5, column=6),
                CellIndex(row=5, column=8),
            ],
        ),
    ],
)
def test_get_neighbours_in_box(cell: CellIndex, expected_result: CellIndex) -> None:
    # Act
    result = get_neighbours_in_box(cell)

    # Assert
    assert result == expected_result
