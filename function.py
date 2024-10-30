def count(a):
    digits = 0
    letters = 0
    symbols = 0
    for i in a:
        if i.isdigit():
            digits += 1

        elif i.isalpha():
            letters += 1
        else:
            symbols += 1
    return digits, letters, symbols
