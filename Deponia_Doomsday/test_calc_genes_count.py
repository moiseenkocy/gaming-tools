from typing import List

import pytest

from achievement_1001_jackalopes import calc_genes_count


@pytest.mark.parametrize(
    "dna, expected_result",
    [([0, 0, 0], 1), ([0, 1, 1, 0], 2), ([1, 2, 2], 2), ([1, 2, 0, 1, 0, 1], 3)],
)
def test_calc_genes_count(dna: List[int], expected_result: int,) -> None:
    result = calc_genes_count(dna)

    assert result == expected_result
