import random

DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SYMBOLS = "!#$%&*+-=?@^_"

chars = ""
accept = "yYдД"


total = input("Сколько паролей нужно? ")
while total not in DIGITS:
    print("Ошибка, введите корректное количество паролей")
    total = input()
length = input("Какова длина пароля? ")
while length not in DIGITS:
    print("Ошибка, введите корректную длину пароля")
    length = input()
digit = input("Включить ли цифры? Y/N: ")
lower = input("Включить ли прописные буквы? Y/N: ")
upper = input("Включаит ли сточные буквы? Y/N: ")
symbols = input("Включать ли спец символы? Y/N: ")
similar_symbols = input("Исключать ли неодназначные символы? (il1Lo0O) Y/N: ")

if digit in accept:
    chars += DIGITS
if lower in accept:
    chars += LOWERCASE_LETTERS
if upper in accept:
    chars += UPPERCASE_LETTERS
if symbols in accept:
    chars += SYMBOLS
if similar_symbols in accept:
    for c in "il1Lo0O":
        chars = chars.replace(c, "")


def pass_gen(total, len):
    for _ in range(total):
        print(*random.sample(chars, len), sep="")


while True:
    pass_gen(int(total), int(length))
    print("Сделать новую связку паролей? Y/N:")
    a = input()
    if a not in accept:
        break
