import MorseCoder

stillContinue = True

while stillContinue:

    answer = ''
    while answer != 'D' and answer != 'E':
        answer = input("Do you wanna Encode to Morse Code, or Decode from Morse Code: (E - Encode / D - Decode)")
        answer = answer.upper()

        if answer != 'D' and answer != 'E':
            print('Invalid Option. Please Try Again.')

    resultPhase = ''

    if answer == 'E':
        text = input("Tell me a phase to translate to Morse Code: ")
        text = text.upper()

        resultPhase = MorseCoder.tomorsecode(text)
    else:
        text = input("Tell me a phase to translate from Morse Code "
                     "(each code must be separated by a space, exemple: ... --- ...): ")
        resultPhase = MorseCoder.frommorsecode(text)

    print(f"Your phase must be: {resultPhase}")

    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = input("Wanna translate another phase? (Y/N)")
        answer = answer.upper()

        if answer == 'N':
            stillContinue = False
            break

        if answer == 'Y':
            break

        print('Invalid Option. Please Try Again.')
