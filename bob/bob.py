def response(hey_bob: str):
    hey_bob = hey_bob.strip()
    
    if hey_bob == '':
        return 'Fine. Be that way!'
    if hey_bob == hey_bob.upper() and hey_bob[-1] == '?':
        return "Calm down, I know what I'm doing!"
    if hey_bob == hey_bob.upper():
        return 'Whoa, chill out!'
        
    else:
        return 'Whatever.'
    
    
mel = 'mel'
print(mel[-1])


