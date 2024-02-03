from helping_func import *


def task_4(name_file: str):
    """
    Генерирует пароли

    :param name_file: Название файла
    :return: Ничего
    """
    file = opening_file(name_file)
    st_row = file[0][:-1]
    st_row += "*password"
    print(st_row)
    result = []
    result.append(st_row)
    file = file[1:]
    for row in file:
        name_ship, num_ship = row[0], row[1]
        home_planet = row[2]
        x_coord, y_coord = row[3], row[4]
        x_direction, y_direction = row[5], row[6]
        password = home_planet[-3:].upper() + name_ship[1:3][::-1] + home_planet[:3][::-1].upper()

        result.append(f"{name_ship}-{num_ship}*{home_planet}*{x_coord} {y_coord}*{x_direction} {y_direction}*{password}")
    writing_file("space_uniq_password.csv", result)
