MorseCode = {'A': '.-',
             'B': '-...',
             'C': '-.-.',
             'D': '-..',
             'E': '.',
             'F': '..-.',
             'G': '--.',
             'H': '....',
             'I': '..',
             'J': '.---',
             'K': '-.-',
             'L': '.-..',
             'M': '--',
             'N': '-.',
             'O': '---',
             'P': '.--.',
             'Q': '--.-',
             'R': '.-.',
             'S': '...',
             'T': '-',
             'U': '..-',
             'V': '...-',
             'W': '.--',
             'X': '-..-',
             'Y': '-.--',
             'Z': '--..',
             '1': '.----',
             '2': '..---',
             '3': '...--',
             '4': '....-',
             '5': '.....',
             '6': '-....',
             '7': '--...',
             '8': '---..',
             '9': '----.',
             '0': '-----'}


def tomorsecode(text: str) -> str:
    morsecodetext = ''
    morsecodetext += ''.join([MorseCode.get(letter) + " " for letter in text])

    return morsecodetext


def frommorsecode(text: str) -> str:

    text = str.split(text, ' ')

    morsecodetext = ''
    morsecodetext += ''.join([list(MorseCode.keys())[list(MorseCode.values()).index(letter)] for letter in text])

    return morsecodetext
