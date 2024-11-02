from function import search_word

text = input("\033[92mEnter a text : ")
word = input("\033[92mEnter the word you want to find : ")

result = search_word(text, word)
print(result)