def to_rna(dna_strand):
    nucs = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna_strand = ''

    for nuc in list(dna_strand):
        rna_strand += nucs[nuc]

    return rna_strand

