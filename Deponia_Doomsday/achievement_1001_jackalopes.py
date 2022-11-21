#!/usr/bin/env python3

from typing import List

DNA_LENGTH = 5

CARTRIDGES = {
    0: "BLUE #1",
    1: "YELLOW #2",
    2: "RED: #3",
}

# These symbols are used in print_genome function
GENES = [
    "0",  # Pet's genes
    "1",  # Clown's genes
    "2",  # Fewlock's genes
]


def sprintf_dna(dna: List[int]) -> str:
    """Convert DNA represented as list of indexes to string."""
    return " ".join([GENES[gene] for gene in dna])


def generate_dna_combinations(dna_length: int, genes: List[int]) -> List[List[int]]:
    """Generate all possible DNA combinations of genes with specified length."""
    sorted_genes = sorted(genes)
    if dna_length == 1:
        return [[x] for x in sorted_genes]

    shorter_dna_list = generate_dna_combinations(dna_length - 1, genes)

    return [[head] + tail for head in sorted_genes for tail in shorter_dna_list]


def generate_gene_locations(
    genes_num: int, available_locations: List[int]
) -> List[int]:
    """Generate all possible locations for specified gene based on its copies number."""
    sorted_locations = sorted(available_locations)

    if genes_num == 1:
        return [[loc] for loc in sorted_locations]

    return [
        [head] + tail
        for head in sorted_locations
        for tail in generate_gene_locations(
            genes_num - 1, [x for x in set(sorted_locations) - set([head]) if x > head]
        )
    ]


def build_dna_with_fixed_gene(
    fixed_gene: int, fixed_gene_locations: List[int], other_genes_seq: List[int]
) -> List[int]:
    """  """
    dna_length = len(other_genes_seq) + len(fixed_gene_locations)
    dna = [None] * dna_length

    all_gene_locations = list(range(dna_length))
    other_genes_locations = sorted(set(all_gene_locations) - set(fixed_gene_locations))

    for i in fixed_gene_locations:
        dna[i] = fixed_gene

    for other_gene, other_gene_location in zip(other_genes_seq, other_genes_locations):
        dna[other_gene_location] = other_gene

    return dna


def generate_dna_with_fixed_genes(
    dna_length: int, fixed_gene: int, fixed_genes_num: int, other_genes: List[int],
) -> List[List[int]]:
    """Generate all possible combinations of DNA with 3 genes with one of them fixed in specific locations."""
    return [
        build_dna_with_fixed_gene(fixed_gene, fixed_gene_locations, other_genes_seq)
        for fixed_gene_locations in generate_gene_locations(
            genes_num=fixed_genes_num, available_locations=list(range(dna_length))
        )
        for other_genes_seq in generate_dna_combinations(
            dna_length - fixed_genes_num, other_genes
        )
    ]


def calc_genes_count(dna: List[int]) -> int:
    """Calculate number of different genes in DNA."""
    return len(set(dna))


if __name__ == "__main__":
    # The most simple case: we use only 2 sets of genes
    for gene_1, gene_2 in [(0, 1), (0, 2), (1, 2)]:
        print(f"TWO GENES: ['{GENES[gene_1]}', '{GENES[gene_2]}']")
        for dna in generate_dna_combinations(
            dna_length=DNA_LENGTH, genes=[gene_1, gene_2]
        ):
            print(sprintf_dna(dna))
        print()

    # Three genes
    fixed_gene = 2
    for fixed_gene_num in range(1, DNA_LENGTH - 1):
        print(f"THREE GENES: '{GENES[fixed_gene]}' x {fixed_gene_num} times")
        for dna in generate_dna_with_fixed_genes(
            dna_length=DNA_LENGTH,
            fixed_gene=fixed_gene,
            fixed_genes_num=fixed_gene_num,
            other_genes=[0, 1],
        ):
            if calc_genes_count(dna) == 3:
                print(sprintf_dna(dna))
        print()
