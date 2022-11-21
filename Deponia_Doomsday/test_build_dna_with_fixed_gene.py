from typing import List

import pytest

from achievement_1001_jackalopes import build_dna_with_fixed_gene


@pytest.mark.parametrize(
    "fixed_gene, fixed_gene_locations, other_genes_seq, expected_result",
    [
        (2, [0, 1], [1, 1, 0], [2, 2, 1, 1, 0]),
        (2, [2, 4], [0, 1, 1, 0], [0, 1, 2, 1, 2, 0]),
        (1, [1], [0, 2, 2, 0], [0, 1, 2, 2, 0]),
    ],
)
def test_build_dna_with_fixed_gene(
    fixed_gene: int,
    fixed_gene_locations: List[int],
    other_genes_seq: List[int],
    expected_result: List[int],
) -> None:
    result = build_dna_with_fixed_gene(
        fixed_gene, fixed_gene_locations, other_genes_seq
    )

    assert result == expected_result
