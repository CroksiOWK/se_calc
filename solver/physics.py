import math


class Physics:
    h = 6.6*10**-34

    def __init__(self, var) -> None:
        super().__init__()

        match var:
            case "m":
                with open("physic_measurement_m", "r") as file:
                    file_m = file.readlines()
                    for l in file_m:
                        print(l, end="")

                    print()
                    print()

                    measurement = int(input("Выберите формулу для решения (её номер): "))

                    match measurement:
                        case 1:
                            self.mass_from_p_and_v()
                        case 2:
                            self.mass_from_f_and_a()
                        case 3:
                            self.mass_from_w_and_g()
                        case 4:
                            self.mass_from_h_and_v()
                        case _:
                            print("Чувака, ты ошибся числом: я такого не умею")

    def mass_from_h_and_v(self):
        λ = float(input("λ: "))
        c = 300000000

        print(f"m = { self.h } / ({ λ } * { c }) = { self.h  / ( λ * c ) }")

    def mass_from_w_and_g(self):
        w = float(input("W: "))
        g = float(input("g: "))
        print(f"m = { w } / { g } = { w / g }")

    def mass_from_f_and_a(self):
        newton = int(input("Введите силу (Ньютоны): "))
        a = int(input("Введите ускорение: "))
        print(f"m = { newton } / { a } = { newton / a }")

    def mass_from_p_and_v(self):
        p = int(input("Введите плотность (p): "))
        volume = int(input("Введите объем (V): "))
        print(f"m = {p} * {volume} = {p * volume}")
