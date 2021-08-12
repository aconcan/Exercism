# Using pointers
def reverse(text):
    i = 0
    j = len(text)-1 
    text = list(text)

    while j > i and text is not None:
        text[i], text[j] = text[j], text[i]
        i += 1
        j -= 1

    return ''.join(text) 

''' 
# Using string splicing:

def reverse(string=''): 
    return string[::-1]

'''

    

