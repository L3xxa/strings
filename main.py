from function import count

a = input("Що-небудь: ")
result_digits, result_letters, result_symbols = count(a)

print("Кількість цифр:", result_digits)
print("Кількість букв:", result_letters)
print("Кількість інших символів:", result_symbols)
