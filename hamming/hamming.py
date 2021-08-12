def distance(strand_a: str, strand_b: str) -> int:
    
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be the same length')
        
    return sum(a!=b for a, b in zip(strand_a, strand_b)) 

# Initial attempt:

# for index, letter in enumerate(strand_a):
#         if letter != strand_b[index]:
#             count += 1          
