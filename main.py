import math

from solver.algebra import Algebra
from solver.geometry import Geometry
from solver.physics import Physics

print("")
console = input("Нажмите любую клавишу чтобы начать. 'exit' - чтобы выйти. ")

while console != "exit":
    console = input("Физика / алгебра / геометрия / астрофизика (в разработке): ")
    direction = str.lower(console)
# test line
    if direction in ["алгебра"]:
        print("Простейшая математика: \n1 - сложение, вычитание, деление и умножение значений\n2 - базовая алгебра (5-9 классы)\n3 - вышмат")
        dir_mat = input("Ваш авыбор: ")
        Algebra(dir_mat)
    elif direction in ["геометрия", "геом"]:
        Geometry()
    elif direction in ["физика", "физ"]:
        # var = input("Какую единицу измерений вам надо найти? ")
        # print("Вводить на английской раскладке и в системе СИ!!!")
        Physics("m")
    elif direction in ["астрофизика"]:
        print("Пока что не сделано.")
    else:
        print("Чет не то ввел.")


