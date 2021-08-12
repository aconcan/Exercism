song_number = {1: ['first', "and a Partridge in a Pear Tree."],
        2: ['second', "two Turtle Doves, "],
        3: ['third', "three French Hens, "],
        4: ['fourth', "four Calling Birds, "],
        5: ['fifth', "five Gold Rings, "],
        6: ['sixth', "six Geese-a-Laying, "],
        7: ['seventh', "seven Swans-a-Swimming, "],
        8: ['eighth', "eight Maids-a-Milking, "],
        9: ['ninth', "nine Ladies Dancing, "],
        10: ['tenth', "ten Lords-a-Leaping, "],
        11: ['eleventh', "eleven Pipers Piping, "],
        12: ['twelfth', "twelve Drummers Drumming, "]
        }

def recite(s, e):
    output = []
    for n in range(s, e + 1):
        output.append(recite_verse(n))
    return output

def recite_verse(n):
    v = f"On the {song_number[n][0]} day of Christmas my true love gave to me: "

    for i in range(n, 0, -1):
        v += f'{song_number[i][1]}'

    return v.replace('and ', '') if n == 1 else v

print(recite(1, 2))
