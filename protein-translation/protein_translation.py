codons = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
}

def proteins(strand):
    result = []
    stops = ['UAA', 'UAG', 'UGA']

    for i in range(0, len(strand), 3):
        if strand[i:i+3] in stops:
            return result
        else:
            result.append(codons[strand[i:i+3]])
    
    return result

