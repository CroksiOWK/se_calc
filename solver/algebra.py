import math


class Algebra:
    def __init__(self, dir_mat) -> None:
        super().__init__()
        try:
            if dir_mat in ["1"]:
                self.basic()
            elif dir_mat in ["2"]:
                self.extended()
        except ValueError:
            print("Неверный тип полученных данных.")
        except ZeroDivisionError:
            print(f"Делить на нуль нельзя.")

    def basic(self):
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))

        print(f"{a} + {b} = {a + b}")
        print(f"{a} - {b} = {a - b}")
        print(f"{a} * {b} = {a * b}")
        print(f"{a} / {b} = {a / b}")

    def extended(self):
        print("Что именно? ")
        with open("algebra", "r") as file:
            algebra = file.readlines()  # нормально не выводит файл

            for l in algebra:
                print(l, end="")

            print()

            algebra_inp = input("Введите номер пункта: ")
            algebra_in = str.lower(algebra_inp)

            match algebra_in:
                case "0":
                    print("Я же написал что пока что не сделано. Я вообще вряд ли за это возьмусь, я не безумец.")
                case "1":
                    self.square_root()
                case "2":
                    self.power()
                case "3":
                    self.quadratic()
                case "4":
                    self.cubic()
                case _:
                    print("Чувака, ты ошибся числом: я такого не умею")

    def square_root(self):
        num = int(input("Введите число для извлечения его корня: "))
        print(f"√{num} = {math.sqrt(num)}")

    def cubic(self):
        xi = 0
        eps = 0.0000000000000000000000001

        print("A*x^3 + B*x^2 + C*x + D")

        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        d = float(input("D: "))

        cnt = 0

        while True and cnt <= 1000:
            cnt += 1
            f = a * xi * xi * xi + b * xi * xi + c * xi + d
            df = 3 * a * xi * xi + 2 * b * xi + c

            print(f"{cnt}. xi={xi} f={f} eps={eps}")

            if abs(f) <= eps:
                break

            xi = xi - f / df

        print(f"{ a }*x^3{b:+}*x^2{c:+}*x{d:+}")

    def quadratic(self):
        print("Формула нахождения Дискриминанта: D = b^2 - 4ac")

        a = int(input("Введите a в данной формуле: "))
        b = int(input("Введите b в данной формуле: "))
        c = int(input("Введите c в данной формуле: "))

        discriminant = (b ** 2) - (4 * a * c)

        print(f"D = {b}^2 - 4*{a}*{c} = {discriminant}")

        if discriminant < 0:
            print("D < 0")
            print("Корней нет.")
        elif discriminant == 0:
            print("D = 0")
            print(f"x = -b / 2a = -{b} / 2*{a} = {-b / (2 * a)}")
        elif discriminant > 0:
            print("D > 0")
            print(f"x = (-b + √D) / 2a = {(-b + math.sqrt(discriminant)) / 2 * a}")
            print(f"x = (-b - √D) / 2a = {(-b - math.sqrt(discriminant)) / 2 * a}")

    def power(self):
        num = int(input("Введите число для возведения его в степень: "))
        degree = int(input("В какую степень возвести число: "))
        print(f"{num}^{degree} = {num ** degree}")
