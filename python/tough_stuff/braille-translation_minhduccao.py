# Based on final instructions and test cases by aidanconnolly
# Assumes plain text string without punctuation
def brailleTrans(s):
    """Translates a non-punctuated string into braille"""
    # Dictionary of conversions is required because going from letters to braille
    # isn't based on a pattern unlike binary
    brailleAlphabet = {
        'CAPS': '000001',       # Signifies capitalization
        ' ': '000000',          # Space character
        'a': '100000',
        'b': '110000',
        'c': '100100',
        'd': '100110',
        'e': '100010',
        'f': '110100',
        'g': '110110',
        'h': '110010',
        'i': '010100',
        'j': '010110',
        'k': '101000',
        'l': '111000',
        'm': '101100',
        'n': '101110',
        'o': '101010',
        'p': '111100',
        'q': '111110',
        'r': '111010',
        's': '011100',
        't': '011110',
        'u': '101001',
        'v': '111001',
        'w': '010111',
        'x': '101101',
        'y': '101111',
        'z': '101011'
    }

    letters = list(s)               # Change word into list of letters
    out = ''
    for letter in letters:          # Letter-by-letter translation
        if letter.isupper():        # Checks if letter is capitalized to insert capital character
            out += brailleAlphabet['CAPS']
        out += brailleAlphabet[letter.lower()]
    return out
