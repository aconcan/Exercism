from string import ascii_lowercase

def is_pangram(sentence):
    
    for letter in ascii_lowercase:
        if letter not in sentence.lower():
            return False
    
    return True

