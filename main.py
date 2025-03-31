def check_pythagorean(a, b, c):
    #Проверяет, выполняется ли теорема Пифагора для трёх чисел
    return a**2 + b**2 == c**2

if __name__ == "__main__":
    print("Введите три числа:")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    if check_pythagorean(a, b, c):
        print("Числа удовлетворяют теореме Пифагора!")
    else:
        print("Числа НЕ удовлетворяют теореме Пифагора.")
