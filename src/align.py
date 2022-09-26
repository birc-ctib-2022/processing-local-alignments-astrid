"""A module for translating between alignments and edits sequences."""


from operator import le
from re import I


def align(x: str, y: str, edits: str) -> tuple[str, str]:
    """Align two sequences from a sequence of edits.

    Args:
        x (str): The first sequence to align.
        y (str): The second sequence to align
        edits (str): The list of edits to apply, given as a string

    Returns:
        tuple[str, str]: The two rows in the pairwise alignment

    >>> align("ACCACAGTCATA", "ACAGAGTACAAA", "MDMMMMMMIMMMM")
    ('ACCACAGT-CATA', 'A-CAGAGTACAAA')

    """
    x_align = ''
    y_align = ''
    i = 0
    j = 0

    for ed in edits:

        if ed == 'M':
            x_align += x[i]
            y_align += y[j]
            i += 1
            j += 1

        elif ed == 'I':
            x_align += '-'
            y_align += y[j]
            j += 1
            
        elif ed == 'D':
            y_align += '-'
            x_align += x[i]
            i += 1

    return x_align, y_align


def edits(x: str, y: str) -> str:
    """Extract the edit operations from a pairwise alignment.

    Args:
        x (str): The first row in the pairwise alignment.
        y (str): The second row in the pairwise alignment.

    Returns:
        str: The list of edit operations as a string.

    >>> edits('ACCACAGT-CATA', 'A-CAGAGTACAAA')
    'MDMMMMMMIMMMM'

    """
    edits = ''
    
    for i in range(len(x)):

        if x[i] != '-' and y[i] != '-':
            edits += 'M'

        elif x[i] == '-':
            edits += 'I'

        elif y[i] == '-':
            edits += 'D'

    return edits

# print(align("ACCACAGTCATA", "ACAGAGTACAAA", "MDMMMMMMIMMMM"))
# print(edits('ACCACAGT-CATA', 'A-CAGAGTACAAA'))
# print(edits("acca-aagt--a", "a-caaatgtcca"))