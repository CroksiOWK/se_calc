import math


class Geometry:
    def __init__(self) -> None:
        super().__init__()

        try:
            basic_math_geom = input("Что именно вас интересует? ")
            geom = str.lower(basic_math_geom)
            match geom:
                case "площади":
                    self.square()
                case "теоремы":
                    self.theorems()
                case "формулы":
                    self.formulas()
                case _:
                    print("Чувака, ты ошибся числом: я такого не умею")

        except ValueError:
            print("Неверный тип данных.")
        except ZeroDivisionError:
            print("На нуль делить нельзя.")

    def square_square(self):
        print("Формула нахождения площади квадрата: S = a^2")
        a = int(input("Введите a в данной формуле: "))
        print(f"S квадрата = a^2 = {a ** 2}")

    def square_rectangle(self):
        print("Формула нахождения площади прямоугольника: S = a * b")
        a = int(input("Введите a в данной формуле: "))
        b = int(input("Введите b в данной формуле: "))
        print(f"S прямоугольника = {a} * {b} = {a * b}")

    def square_rhombus(self):
        print("1-ая формула нахождения площади ромба: S = a × h ")
        print("2-ая формула нахождения площади ромба: (d₁ × d₂) / 2 ")
        formula = input("По какой формуле будете находить S ромба?(1-ая, 2-ая, обе?) ")
        form = str.lower(formula)

        if form in ["1-ая", "первая", "обе"]:
            a = int(input("Введите a в данной формуле: "))
            h = int(input("Введите h в данной формуле: "))
            print(f"S ромба(по первой формуле) = {a} * {h} = {a * h}")
        if form in ["2-ая", "вторая", "обе"]:
            d1 = int(input("Введите d1 в данной формуле: "))
            d2 = int(input("Введите d2 в данной формуле: "))
            print(f"S ромба(по второй формуле) = ({d1} × {d2}) / 2 = {(d1 * d2) / 2}")

    def square_trapezoid(self):
        print("Формула нахождения площади трапеции: S = 1/2 × (a + b) × h")
        a = int(input("Введите a в данной формуле: "))
        b = int(input("Введите b в данной формуле: "))
        h = int(input("Введите h в данной формуле: "))
        print(f"S трапеции = 1/2 * ({a} + {b}) * {h} = {1 / 2 * (a + b) * h}")


    def square_parallelogram(self):
        print("Формула нахождения площади параллелограмма: S = a × h")
        a = int(input("Введите a в данной формуле: "))
        h = int(input("Введите h в данной формуле: "))
        print(f"S параллелограмма = {a} * {h} = {a * h}")

    def square_triangle_regular(self):
        print("1-ая формула нахождения площади правильного треугольника: (с² × √3) / 4")
        print("2-ая формула нахождения площади правильного треугольника: (с × h) / 2")

        formula = input("По какой формуле будете находить S ромба?(1-ая, 2-ая, обе?) ")
        form = str.lower(formula)
        c = int(input("Введите c в данной формуле: "))

        if form in ["1-ая", "первая", "обе"]:
            print(
                f"S правильного треугольника (по первой формуле) = ({c}² × √3) / 4 = {((c ** 2) * math.sqrt(3)) / 4}")

        if form in ["2-ая", "вторая", "обе"]:
            h = int(input("Введите h в данной формуле: "))
            print(f"S правильного треугольника (по первой формуле) = ({c} × {h}) / 2 = {(c * h) / 2}")

    def square_triangle_right(self):
        print("Формула нахождения площади прямоугольного треугольника: S = (a × b) / 2")
        a = int(input("Введите a в данной формуле: "))
        b = int(input("Введите b в данной формуле: "))
        print(f"S прямоугольного треугольника = ({a} * {b}) / 2 = {(a * b) / 2}")

    def square_triangle_irregular(self):
        # Добавить возможность решения с разными формулами
        print("1-ая формула площади произвольного треугольника: S = (a × h) / 2")
        print("2-ая формула площади произвольного треугольника: S = (a × b) * sin(A)")
        a = int(input("Введите a в данной формуле: "))
        b = int(input("Введите b в данной формуле: "))
        h = int(input("Введите h в данной формуле: "))
        sin = int(input("Введите угол между сторонами a и b: "))
        print(f"S хаотичного треугольника = ({a} * {h}) / 2 = {(a * h / 2)}")
        print(f"S хаотичного треугольника = ({a} * {b}) / sin({sin}) = {(a * b) / math.sin(sin)}")

    def circle(self):
        print("Во имя простоты число Пи было округлено до 3.14. Учитывайте это при вычислениях.")
        print("P.S.: L - длина окружности")
        print("1-ая формула нахождения площади круга: S = π × r²")
        print("2-ая формула нахождения площади круга: S = (π × d²) / 4")
        print("3-ая формула нахождения площади круга: S = L² : (4 × π)")

        formula = input(
            "По какой формуле будете находить S ромба?(1-ая; 2-ая; 3-ая; 1,2; 1,3; 2,3; все три?) ")
        form = str.lower(formula)

        if form in ["1-ая", "1,2", "1,3", "все три"]:
            r = int(input("Введите r в первой формуле: "))
            print(f"S круга по первой формуле = 3.14 × {r}² = {3.14 * (r ** 2)}")
        if form in ["2-ая", "1,2", "2,3", "все три"]:
            d = int(input("Введите d во второй формуле: "))
            print(f"S круга по второй формуле = (3.14 × {d}²) / 4 = {(3.14 * (d ** 2)) / 4}")
        if form in ["3-ая", "1,3", "2,3", "все три"]:
            r = int(input("Введите L в третьей формуле: "))
            print(f"S круга по третьей формуле = L² : (4 × π)")

    def square(self):
        print("Площадь чего именно?")
        with open("square", "r") as file:
            square = file.readlines()
            print(square)
            square_in = input("Выберите площадь: ")
            square_inp = str.lower(square_in)
            match square_inp:
                case "1":
                    self.square_square()
                case "2":
                    self.square_rectangle()
                case "3":
                    self.square_rhombus()
                case "4":
                    self.square_trapezoid()
                case "5":
                    self.square_parallelogram()
                case "6":
                    self.square_triangle_regular()
                case "7":
                    self.square_triangle_irregular()
                case "8":
                    self.square_triangle_right()
                case "9":
                    self.circle()
                case _:
                    print("Чувака, ты ошибся числом: я такого не умею")

    def theorems(self):
        print("Какая именно теорема?")
        with open("theorem", "r") as file:
            theorem = file.readlines()
            print(theorem)
            theorem_in = input("Введите номер (из предложенного списка) теоремы: ")
            theorem = str.lower(theorem_in)

            match theorem:
                case "1":
                    self.pifagor()
                case _:
                    print("Чувака, ты ошибся числом: я такого не умею")

    def pifagor(self):
        print("Теорема Пифагора: a^2 + b^2 = c^2")
        print("обратная теорема теореме Пифагора: c^2 = a^2 + b^2")
        teor_Pif = input("Что именно вам нужно найти? ")
        teor = str.lower(teor_Pif)

        if teor in ["c", "с"]:
            a = int(input("Введите a в данной формуле: "))
            b = int(input("Введите b в данной формуле: "))
            c = (a ** 2) + (b ** 2)
            print(f"c^2 = {a}^2 + {b}^2 = {c}")
            print(f"c = √{c} = {math.sqrt(c)}")

        if teor in ["a", "b", "а", "б"]:
            c = int(input("Введите c в данной формуле: "))
            x = int(input("Введите b(или a, если вы ввели a) в данной формуле: "))
            y = (c ** 2) - (x ** 2)

            print(f"a^2(или b, если вы ввели b) = c^2 - b^2 = {c}^2 - {x}^2 = {y}")
            print(f"a(или b, если вы ввели b) = √{y} = {math.sqrt(y)}")

    def formulas(self):
        print("Какая именно?")
        with open("formula", "r") as file:
            formula0 = file.readlines()
            print(formula0)
            formula_in = input("Введите номер(из предложенного списка) формулы: ")
            formula = str.lower(formula_in)
            match formula:
                case "1":  # Формула Герона
                    self.heron()
                case "2":  # Формула полупериметра
                    self.halfper()
                case "3":
                    self.trigonodmetry()
                case _:
                    print("Чувака, ты ошибся числом: я такого не умею")

    def heron(self):
        print("Формула Герона для нахождения площади треугольника: S = √(p × (p - a) × (p - b) × (p - c))")
        a = int(input("Введите a в данной формуле: "))
        b = int(input("Введите b в данной формуле: "))
        c = int(input("Введите c в данной формуле: "))
        p = int(input("Введите p в данной формуле(если p не известен введите 0): "))

        if p == 0:
            p = (a + b + c) / 2
            print(f"p = (a + b + c) / 2 = ({a} + {b} + {c}) / 2 = {p}")
            print(
                f"S = √({p} × ({p} - {a}) × ({p} - {b}) × ({p} - {c})) = {math.sqrt(p * (p - a) * (p - b) * (p - c))}")
        else:
            print(
                f"S = √({p} × ({p} - {a}) × ({p} - {b}) × ({p} - {c})) = {math.sqrt(p * (p - a) * (p - b) * (p - c))}")

    def halfper(self):
        print("Формула нахождения полупериметра = (a + b + c) / 2")
        a = int(input("Введите a в данной формуле: "))
        b = int(input("Введите b в данной формуле: "))
        c = int(input("Введите c в данной формуле: "))
        p = (a + b + c) / 2
        print(f"p = (a + b + c) / 2 = ({a} + {b} + {c}) / 2 = {p}")

    def trigonodmetry(self):
        corner = int(input("Введите угол между стороной a и b: "))
        print(f"синус - {math.sin(corner)}")
        print(f"косинус - {math.cos(corner)}")
        print(f"тангес - {math.tan(corner)}")
        print(f"котангес - {math.cos(corner) / math.sin(corner)}")
