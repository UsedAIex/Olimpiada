from helping_func import *


def task_1(name_file: str) -> None:
    """
    Функция переписывает нулевые координаты последнего места связи.
    Она ничего не возврацает, только выводит на экран строку вида

        {name_ship}-{num_ship} - {x_coord} {y_coord},

    где name_ship - Код корабля,num_ship - номер корабля, x_coord, y_coord - координаты последнего места связи

    :param name_file: Название файла
    :return: Ничего
    """

    file = opening_file(name_file)
    new_data = [file[0]]
    file = file[1:]
    for row in file:
        name_ship, num_ship = row[0], row[1]
        home_planet = row[2]
        x_coord, y_coord = row[3], row[4]
        x_direction, y_direction = row[5], row[6]

        n = int(num_ship[0])
        m = int(num_ship[1])
        t = len(home_planet)
        if x_coord == 0 and y_coord == 0:
            if n > 5:
                x_coord = n + x_direction
            else:
                x_coord = -1 * (n + x_direction) * 4 + t

            if m > 3:
                y_coord = m + t + y_direction
            else:
                y_coord = -1 * (n + y_direction) * m
        # BЭSD-149*Чавланшан*-76 -60*0 4

        new_data.append(f"{name_ship}-{num_ship}*{home_planet}*{x_coord} {y_coord}*{x_direction} {y_direction}")
        if name_ship[-1] == "V":
            print(f"{name_ship}-{num_ship} - {x_coord} {y_coord}")

    writing_file("space_new.txt", new_data)
