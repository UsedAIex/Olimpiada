from helping_func import *


def task_3(name_file: str) -> None:
    """
    Ищет корабля корабль, который хочет пользователь
    Если нашелся такой корабль то выводит строку формата:

        Корабль {ShipName} был отправлен с планеты: {planet} и его направление движения было: {direction},

    где ShipName - название корабля, planet - навание родной планеты, direction - направление движения


    :param name_file: Название файла
    :return: Ничего
    """
    file = opening_file(name_file)
    n_ship = input()
    while n_ship != "stop":
        for row in file:
            if (row[0] + "-" + row[1]) == n_ship:
                st = (f"Корабль {row[0]}-{row[1]} был отправлен с планеты: {row[2]} и "
                      f"его направление движения было: {row[5]} {row[6]}")

                print(st)
                break
        else:
            print("error.. er.. ror..")
        n_ship = input()


