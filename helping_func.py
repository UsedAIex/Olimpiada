def opening_file(name: str) -> list:
    """

    Функция открывает файл, берет оттуда все строки и записывает отдельный список код корабля,
    его номер, родную планету, координаты последнего места связи и направление движения

    Возвращает список со всеми данными, включая самую первую строку
    :param name: Название файла
    :return: Возвращает список со всеми данными, включая самую первую строку
    """
    file = open(name, encoding="UTF-8")
    st_row = file.readline()
    result = []
    result.append(st_row)
    for row in file.readlines():
        if row[-1] == "\n":
            row = row[:-1]
        znach = row.split("*")
        kod_ship, num_ship = znach[0].split("-")
        home_planet = znach[1]
        x_coord, y_coord = znach[2].split()
        x_direction, y_direction = znach[3].split()
        result.append([kod_ship, num_ship, home_planet, x_coord, y_coord, x_direction, y_direction])
    file.close()
    return result


def writing_file(name: str, data: list) -> None:
    """
    Создает файл и запысывает в него данные

    :param name: Название файла, в который записывают данные
    :param data: Данные
    :return: Ничего
    """
    file_w = open(name, "w", encoding="UTF-8")
    file_w.write(data[0])
    file_w.write("\n")
    data = data[1:]
    for row in data:
        file_w.write(row)
        file_w.write("\n")
    file_w.close()
