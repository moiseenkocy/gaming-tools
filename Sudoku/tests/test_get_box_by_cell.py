import pytest

from sudoku.helpers import CellIndex, get_box_by_cell


@pytest.mark.parametrize(
    "cell, expected_result",
    [
        (CellIndex(row=0, column=0), CellIndex(row=0, column=0)),
        (CellIndex(row=6, column=6), CellIndex(row=6, column=6)),
        (CellIndex(row=4, column=4), CellIndex(row=3, column=3)),
        (CellIndex(row=7, column=5), CellIndex(row=6, column=3)),
    ],
)
def test_get_box_by_cell(cell: CellIndex, expected_result: CellIndex) -> None:
    # Act
    result = get_box_by_cell(cell)

    # Assert
    assert result == expected_result
