import random

print("Добро пожаловать в числовую угадайку")
print("Введите правую границу числа:")

cnt = 0
new_game = ""
max_chislo = int(input())
r_num = random.randrange(1, max_chislo)
print("Введите ваше предположение:")


def ugadaika(n):
    if n < r_num:
        return "Слишком мало, попробуйте еще раз"
    if n > r_num:
        return "Слишком много, попробуйте еще раз"
    else:
        return "Вы угадали, поздравляем!"


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    else:
        return False


while True:
    num = input()
    if is_valid(num):
        cnt += 1
        result = ugadaika(int(num))
        print(result)
        if result == "Вы угадали, поздравляем!":
            print("Количество попыток угадать число:", cnt)
            if cnt > 7:
                print("Что то много ушло у вас попыток...")
            print("Хотите начать новую игру? Y/N:")
            new_game = input()
            if new_game in ("Y", "y", "д", "Д"):
                print("Введите правую границу числа:")
                max_chislo = int(input())
                r_num = random.randrange(1, max_chislo)
                cnt = 0
                print("Начинаем новую игру")
                print("Введите ваше предположение:")
            else:
                break

    else:
        print(f"А может быть все-таки введем целое число от 1 до {max_chislo}?")
