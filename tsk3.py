from helping_func import *


def tsk_3(name_file: str, n_ship: str):
    file = opening_file(name_file)

    for row in file:
        if (row[0] + "-" + row[1]) == n_ship:
            st = (f"Корабль {row[0]}-{row[1]} был отправлен с планеты: {row[2]} и "
                  f"его направление движения было: {row[5]} {row[6]}")

            return st
    else:
        return "error.. er.. ror.."
