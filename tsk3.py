from helping_func import *


def tsk_3(name_file: str):
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


