
def replace_word(text, word, overwrite):

    green_color = '\033[92m'
    reset_color = '\033[0m'

    rep = []
    for i in text.split():
        clean_text = i.strip(" ,./!@#$%^&*()_+=")
        if clean_text == word:
            rep.append(green_color + overwrite + reset_color)
        else:
            rep.append(i)
    return ' ' .join(rep)
















