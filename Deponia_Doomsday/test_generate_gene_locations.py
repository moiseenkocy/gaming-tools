from typing import List

import pytest

from achievement_1001_jackalopes import generate_gene_locations


@pytest.mark.parametrize(
    "genes_num, available_locations, expected_result",
    [
        (1, [0, 1, 2, 3, 4], [[0], [1], [2], [3], [4]]),
        (2, [0, 1, 2, 3], [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]),
        (3, [0, 1, 3, 4], [[0, 1, 3], [0, 1, 4], [0, 3, 4], [1, 3, 4]]),
        (
            3,
            [0, 1, 2, 3, 4],
            [
                [0, 1, 2],
                [0, 1, 3],
                [0, 1, 4],
                [0, 2, 3],
                [0, 2, 4],
                [0, 3, 4],
                [1, 2, 3],
                [1, 2, 4],
                [1, 3, 4],
                [2, 3, 4],
            ],
        ),
    ],
)
def test_generate_gene_locations(
    genes_num: int, available_locations: List[int], expected_result: List[int]
) -> None:
    result = generate_gene_locations(genes_num, available_locations)

    assert result == expected_result
