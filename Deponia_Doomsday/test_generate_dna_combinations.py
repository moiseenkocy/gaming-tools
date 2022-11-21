from typing import List

import pytest

from achievement_1001_jackalopes import generate_dna_combinations


@pytest.mark.parametrize(
    "dna_length, genes, expected_result",
    [
        (2, [0], [[0, 0]]),
        (
            3,
            [0, 1],
            [
                [0, 0, 0],
                [0, 0, 1],
                [0, 1, 0],
                [0, 1, 1],
                [1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1],
            ],
        ),
        (
            2,
            [0, 1, 2],
            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2],],
        ),
    ],
)
def test_generate_dna_combinations(
    dna_length: int, genes: List[int], expected_result: List[List[int]]
) -> None:
    result = generate_dna_combinations(dna_length, genes)

    assert result == expected_result
