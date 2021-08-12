def find_anagrams(word, candidates):        
    word_lower = word.lower()
    return [candidate for candidate in candidates if is_anagram(word_lower, candidate.lower()) is True] 

def is_anagram(word, candidate):
    return word != candidate and sorted(candidate) == sorted(word)
