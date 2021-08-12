def is_isogram(word):

    lower = word.lower()
    return all(lower.count(char) == 1 for char in lower if char.isalpha() is True)
