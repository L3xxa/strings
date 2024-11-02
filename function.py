def search_word(text, word):
    count = 0
    for i in text.split():
        if i == word:
            count += 1
    if count == 0:
        print("The word is not found")
    else:
        print(f"The word is found \033[91m{count}\033[0m  \033[92mtimes\033[0m")
    return count

