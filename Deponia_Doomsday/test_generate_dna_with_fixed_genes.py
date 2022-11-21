from typing import List

import pytest

from achievement_1001_jackalopes import generate_dna_with_fixed_genes


@pytest.mark.parametrize(
    "dna_length, fixed_gene, fixed_genes_num, other_genes, expected_result",
    [
        (
            4,
            2,
            2,
            [0, 1],
            [
                [2, 2, 0, 0],
                [2, 2, 0, 1],
                [2, 2, 1, 0],
                [2, 2, 1, 1],
                [2, 0, 2, 0],
                [2, 0, 2, 1],
                [2, 1, 2, 0],
                [2, 1, 2, 1],
                [2, 0, 0, 2],
                [2, 0, 1, 2],
                [2, 1, 0, 2],
                [2, 1, 1, 2],
                [0, 2, 2, 0],
                [0, 2, 2, 1],
                [1, 2, 2, 0],
                [1, 2, 2, 1],
                [0, 2, 0, 2],
                [0, 2, 1, 2],
                [1, 2, 0, 2],
                [1, 2, 1, 2],
                [0, 0, 2, 2],
                [0, 1, 2, 2],
                [1, 0, 2, 2],
                [1, 1, 2, 2],
            ],
        ),
    ],
)
def test_generate_dna_with_fixed_genes(
    dna_length: int,
    fixed_gene: int,
    fixed_genes_num: int,
    other_genes: List[int],
    expected_result: List[List[int]],
) -> None:
    result = generate_dna_with_fixed_genes(
        dna_length, fixed_gene, fixed_genes_num, other_genes
    )

    assert result == expected_result
